# -*- coding: utf-8 -*-
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

import settings
from db import *

#Стартовое меню - клавиатура
def start_menu_keyboard ():
    inline_keyboard = [[InlineKeyboardButton("Кабинет", callback_data='personal_area'),
                        InlineKeyboardButton("Все курсы", callback_data='courses_menu')],
                       [InlineKeyboardButton("Пригласи друга и заработай", callback_data='referal_menu')],
                       [InlineKeyboardButton("Помощь",callback_data='help_menu'), InlineKeyboardButton("Приват-клуб", callback_data='private')]]
    reply_markup = InlineKeyboardMarkup(inline_keyboard)

    return reply_markup

#Все курсы - клава
def all_courses_keyboard():
    all_courses_key = [[InlineKeyboardButton("Арбитраж", callback_data='all_arbitrage'),
                        InlineKeyboardButton("Схемы", callback_data='all_scheme')],
                       [InlineKeyboardButton("Обучения",callback_data='all_education'), InlineKeyboardButton("Приват-клуб", callback_data='private')],
                       [InlineKeyboardButton("« Назад", callback_data="back_to_start")]]
    reply_markup = InlineKeyboardMarkup(all_courses_key)

    return reply_markup

#Схемы
def all_scheme_keyboard():
    all_schem_key = [[InlineKeyboardButton("Влево", callback_data='product_1'), InlineKeyboardButton("Счетчитк", callback_data='all_scheme'),  InlineKeyboardButton("Вправо", callback_data='all_scheme')],
                    [InlineKeyboardButton("Приобрести",callback_data='buy_1'), InlineKeyboardButton("Скачать", callback_data='private')],
                    [InlineKeyboardButton("« Назад", callback_data="back_to_all_courses")]]
    reply_markup = InlineKeyboardMarkup(all_schem_key)

    return reply_markup


#Карточка товара
def product_keyboard(id_product):

    id_arr_left, id_arr_right, len_indexer, index_product = Product(id_product).get_list()

    id_arr_left = str(id_arr_left)
    id_arr_right = str(id_arr_right)
    len_indexer = str(len_indexer)
    index_product = str(index_product)

    product_key = [[InlineKeyboardButton("Влево", callback_data='product_'+id_arr_left), InlineKeyboardButton(""+index_product+"/"+len_indexer, callback_data='all_scheme'),  InlineKeyboardButton("Вправо", callback_data='product_'+id_arr_right)],
                    [InlineKeyboardButton("Приобрести",callback_data='buy_'+id_product), InlineKeyboardButton("Скачать", callback_data='download_'+id_product)],
                    [InlineKeyboardButton("« Назад", callback_data="back_to_all_courses")]]
    reply_markup = InlineKeyboardMarkup(product_key)

    return reply_markup

#Клавиатура кабинета
def personal_area_keyboard ():
    inline_keyboard = [[InlineKeyboardButton("Вывести баланс", callback_data='personal_area')],
                       [InlineKeyboardButton("Покупки", callback_data='referal_menu')],
                       [InlineKeyboardButton("Назад", callback_data='back_to_start')]
                       ]
    reply_markup = InlineKeyboardMarkup(inline_keyboard)

    return reply_markup