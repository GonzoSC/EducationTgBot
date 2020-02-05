# -*- coding: utf8 -*-
import pymysql
import logging
from operator import itemgetter

import settings

db = pymysql.connect('localhost','slipvlad', '394935', 'educationbot', cursorclass=pymysql.cursors.DictCursor)
db.autocommit(True)

def get_or_create_user(db, effective_user, message):
    cur = db.cursor()
    cur.execute("SELECT * FROM users WHERE user_id = %s", effective_user.id)
    user = cur.fetchone()

    if not user:
        query = "INSERT INTO users (user_id, firstname, lastname, username, chat_id) VALUES (%s,%s,%s,%s,%s)"
        args = (effective_user.id, effective_user.first_name, effective_user.last_name, effective_user.username, message.chat_id)
        cur.execute(query, args)

    return user


## Операции с продуктами
class Product:
    def __init__(self, id_product):
        self.id = id_product

    #получить полную информацию о товаре по айди
    def get_info (self):
        try:
            cur = db.cursor()
            cur.execute("SELECT * FROM product WHERE id = %s", self.id)
            product = cur.fetchone()
            return product

        except SyntaxError as e:
            logging.info(e)

    #получить информацию для формирования витрины
    def get_list(self):
        try:
            product = Product(self.id).get_info()

            cur = db.cursor()
            cur.execute("SELECT * FROM product WHERE category = %s",product['category'])
            product_rows = cur.fetchall()

            #создаем список ид: индекс для всех товаров в нужной категории
            indexer = dict((p['id'], i) for i, p in enumerate(product_rows))

            #берем индекс продукта по его ид
            index_product = indexer.get(product['id'])

            #сколько всего продуктов в категории
            len_indexer = len(indexer)

            #получаем индексы стрелочек
            if index_product == 0:
                index_arrow_left = len_indexer - 1
            else:
                index_arrow_left = index_product - 1

            if index_product == len_indexer - 1:
                index_arrow_right = 0
            else:
                index_arrow_right = index_product + 1

            #получаем id продуктов по их индексу для стрелочек
            id_indexer = dict((i, p['id']) for i, p in enumerate(product_rows))
            id_arrow_left = id_indexer.get(index_arrow_left)
            id_arrow_right = id_indexer.get(index_arrow_right)

            return id_arrow_left, id_arrow_right, len_indexer, index_product+1

        except SyntaxError as e:
            logging.info(e)







