# -*- coding: utf-8 -*-
import logging
import re

from telegram import ReplyKeyboardRemove,  ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, error
from telegram.ext import  ConversationHandler

from db import *
from utils import *


def get_start_menu (bot, update, user_data):
    user = get_or_create_user(db, update.effective_user, update.message)
    update.message.reply_text("Выберите раздел: ", reply_markup=start_menu_keyboard())

def inline_button_pressed (bot, update):
    query = update.callback_query
    print(query.data)

#Раздел Все курсы
    if query.data == "courses_menu" or query.data == "back_to_all_courses":
        text = "Выберите раздел:"
        bot.edit_message_text(text=text, chat_id=query.message.chat.id, message_id=query.message.message_id, reply_markup=all_courses_keyboard())

# Стартовое меню
    if query.data == "back_to_start":
        text = "Выберите раздел:"
        bot.edit_message_text(text=text, chat_id=query.message.chat.id, message_id=query.message.message_id, reply_markup=start_menu_keyboard())

# Раздел Схемы

    #Если квери.дата соответствует регулярке - выводи табличку с продуктом:
    if re.match(r'product_\d+', query.data) is not None:
        id_product =  re.split(r'_', query.data)[1] #получаем айди продукта из переменной квери.дата

        try:
            id_product = int(id_product)
            product = Product(id_product).get_info()

            text = '{} \n{} \n*Цена:* {}'.format(product['name'],product['description'],str(product['price']))
            bot.edit_message_text(text=text, chat_id=query.message.chat.id, message_id=query.message.message_id, parse_mode='Markdown',
                                 reply_markup=product_keyboard(str(id_product)))

        except (TypeError):
            logging.info(TypeError)


    if query.data == "all_scheme":
        text = "Описание, зеркало"
        bot.edit_message_text(text=text, chat_id=query.message.chat.id, message_id=query.message.message_id, reply_markup=all_scheme_keyboard())


#Раздел кабинет
    if query.data == "personal_area":
        user = get_or_create_user(db, update.effective_user, update.message)

        text = """
Имя: {}
Фамилия: {} 
Баланс: {} 
        """.format(user['firstname'], user['lastname'], user['balance'])
        bot.edit_message_text(text=text, chat_id=query.message.chat.id, message_id=query.message.message_id,
                              reply_markup=personal_area_keyboard())
