from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy_log import *


def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')


def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'/hi\n/time\n/help')


def time_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')


def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text  # ~input
    print(msg)
    items = msg.split()  # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x+y}')  # ~print


def delt_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text  # ~input
    text_list = msg.split(" ")
    update.message.reply_text(f'{" ".join([item for item in text_list[1:] if not "абв" in item])}')


def quit_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text  # ~input
    update.message.reply_text('Бот остановлен')
    exit()
