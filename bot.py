from json import dumps
from telebot import TeleBot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from expiringdict import ExpiringDict
from rich import print
from MC import MC

TOKEN = '6158079290:AAGaBazb3qVEiMcfCD3O8rUBOd2cz1zQ2YM'

bot = TeleBot(TOKEN, parse_mode='HTML', threaded=True, num_threads=4, colorful_logs=True)
cache = ExpiringDict(max_len=100000, max_age_seconds=7200)
tool = MC(cache)

extesion_to_filename = {'mp4': 'Video', 'mp3':'Audio'}

@bot.message_handler(commands=['start', 'help'])
def start(message:Message):
    bot.reply_to(message, """""")


@bot.message_handler(regexp=r'^(?:https?:\/\/)?(?:www\.)?(?:m\.)?(?:youtube\.com|youtu\.be)\/(?:(watch)?\?v=|embed\/|v\/|.+\?v=)?([a-zA-Z0-9_-]{11}).*$')
def youtube(message:Message):
    data = tool.youtube.get_data(message.text)
    if not data.get('mess'):
        id = tool.youtube.get_id(message.text)
        t = data.get('t', 0)
        h = int(t/3600) if t>3600 else 0
        m = int((t-(h*3600))/60)
        s = t-(h*3600)-(m*60)
        response = f"""᯽----------᯽----------᯽\n𝐓𝐢𝐭𝐥𝐞: <a href="{message.text}">{data.get('title', '')}</a>\n𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧: {f'{h}s' if h else ''} {f'{"0" if m < 10 else ""}{m}m' if m else ''} {"0" if s < 10 else ""}{s}s\n𝐂𝐡𝐚𝐧𝐧𝐞𝐥: {data.get('a', '')}\n᯽----------᯽----------᯽"""
        reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(extesion_to_filename.get(ext, 'UNKNOWN'), callback_data=dumps({'w': 'y', 'id': id, 'filetype': ext})) for ext in data['links']]])
        bot.send_message(message.chat.id, response, reply_markup=reply_markup)
        

@bot.message_handler(regexp=f'\b((?:https?)://[^\s/$.?#].[^\s]*)\b')
def url_handler(message:Message):
    #Handle all other URLS
    pass


print('Running...')
bot.infinity_polling(restart_on_change=True)


# TODO:
#   1. Create the parent class