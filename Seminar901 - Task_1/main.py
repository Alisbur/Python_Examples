from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *

updater = Updater('5529264334:AAG7goYxffk1H69rmm5IbBXAOL7_iAf_o-U')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))

updater.dispatcher.add_handler(CommandHandler('delt', delt_command))
updater.dispatcher.add_handler(CommandHandler('exit', quit_command))

updater.start_polling()
updater.idle()
