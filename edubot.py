# coding=UTF-8
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler,\
        ConversationHandler, CallbackQueryHandler

from handlers import  *
import settings


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.REQUEST_KWARGS)
    logging.info('Bot starting')

    dp = mybot.dispatcher

    dp.add_handler(CommandHandler("start", get_start_menu, pass_user_data=True))
    dp.add_handler(CallbackQueryHandler(inline_button_pressed))

    mybot.start_polling() #регулярно ходи на телеграм и проверяй обновления
    mybot.idle() #работай до принудительного завершения


if __name__ == "__main__":
    main()