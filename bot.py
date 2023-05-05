from telebot import TeleBot
from telebot.types import Message
from rich import print

TOKEN = '6158079290:AAGaBazb3qVEiMcfCD3O8rUBOd2cz1zQ2YM'

bot = TeleBot(TOKEN, parse_mode='HTML', threaded=True, num_threads=4, colorful_logs=True)


@bot.message_handler(commands=['start', 'help'])
def start(message:Message):
    bot.reply_to(message, "WT")



print('Running...')
bot.infinity_polling(restart_on_change=True)