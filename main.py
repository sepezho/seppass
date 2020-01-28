import telebot
import sys

sys.path.append('./modules')
from start import start_main

telebot.apihelper.proxy = {
	'http': 'socks5://sockduser:f2%kElHW0SEC@46.101.118.222:1080',
	'https': 'socks5://sockduser:f2%kElHW0SEC@46.101.118.222:1080'
}

bot = telebot.TeleBot("1028700604:AAGYy9m51_TGRUCUzGagAQKnKZfTiR0tFk8")

@bot.message_handler(commands=['start'])
def message_handler_start_main(message):
	start_main(message, bot)

bot.polling()