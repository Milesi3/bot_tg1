import models, view
from telegram import Bot
from telegram.ext import Updater, CommandHandler


def run():
    bot_token = '5752718030:AAEBGLw2EdizW2nMPoKnSCUCvYTG4baDFpc'
    updater = Updater(bot_token, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', models.start)
    open_handler = CommandHandler('open', models.open)
    find_handler = models.conv_handler('find', view.find, models.find_output)
    add_row_handler = models.conv_handler('addrow', view.add_row, models.add_row_output)
    delete_handler = models.conv_handler('deleterow', view.deleterow, models.deleterow_output)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(open_handler)
    dispatcher.add_handler(find_handler)
    dispatcher.add_handler(add_row_handler)
    dispatcher.add_handler(delete_handler)

    updater.start_polling()
    updater.idle()