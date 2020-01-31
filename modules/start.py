import os
import gnupg
import sqlite3
from telebot import types

def start_main(message, bot_old):
	global bot
	bot = bot_old
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	markup.add('Вход', 'Регистрация')
	msg = bot.send_message(message.chat.id, 'Привет, '+message.chat.username+' !\nТы новенький или уже имел со мной дело?', reply_markup=markup)
	bot.register_next_step_handler(msg, start_response)

def start_response(message):
	if message.text == 'Вход':
		sign(message)
	elif message.text == 'Регистрация':
		login(message)
	else:
		bot.send_message(message.chat.id, 'Непонел.', reply_markup = types.ReplyKeyboardRemove(selective=False))

def login(message):
	conn = sqlite3.connect('DataBase.db', check_same_thread=False)
	c = conn.cursor()
	query = "SELECT COUNT(*) FROM Users WHERE Username = '" + message.chat.username + "'"
	answer = c.execute(query)
	conn.commit()
	conn.close()

	if answer != 0:
		msg = bot.send_message(message.chat.id, 'Придумайте пароль.', reply_markup = types.ReplyKeyboardRemove(selective=False))
		bot.register_next_step_handler(msg, login_response)
	else:
		bot.send_message(message.chat.id, 'Ваш телеграм уже связан с вашим акк для этого бота.\n\nВойдите в акк, отправив снова /start', reply_markup = types.ReplyKeyboardRemove(selective=False))

def login_response(message):
	# gpg = gnupg.GPG(gnupghome='/home/sepezho/.gnupg/')
	# input_data = gpg.gen_key_input(
	#     passphrase=message.text,
	# 	name_real=message.chat.username)
	# key = gpg.gen_key(input_data)
	# key = key.fingerprint
	key = 'key.fingerprint'

	conn = sqlite3.connect('DataBase.db', check_same_thread=False)
	c = conn.cursor()
	query = "INSERT INTO Users (Username, Password, Settings) VALUES ('"+ message.chat.username +"', '"+key+"', 'obj')"
	c.execute(query)
	conn.commit()
	conn.close()
	# os.mkdir('/home/sepezho/Documents/seppass/Users_folder/' + message.chat.username)
	bot.send_message(message.chat.id, 'Пароль зашифрован и сохранен в БД. Так же создана папка, где ваш никнейм выступил в качестве названия.\n\nПароль:\n'+ message.text +'\n\nЭто ваш отпечаток ключа:\n'+ key)
	settings_begin(message)

def settings_begin(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton(text= 'Я доверяю разрабу. Оставлю все как есть.', callback_data = 'return'))
	markup.add(types.InlineKeyboardButton(text='Я гик. Все настрою сам.', callback_data = 'back'))
	
	bot.send_message(message.chat.id, 'Перейдем к настройкам.', reply_markup = markup)
	@bot.callback_query_handler(func=lambda message: True)
	def pre_setting_list(message):
		settings_list(message)

def settings_list(message):
	if message.data == 'return':
		settings_return(message)
	if message.data == 'to_first_list':
		setting_first_list(message)
	if message.data == 'to_sec_list':
		setting_sec_list(message)
	if message.data == 'finish':
		setting_finish(message)
	if message.data == 'back':
		settings_main(message)

def settings_main(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton(text= 'return', callback_data = 'return'))
	markup.add(types.InlineKeyboardButton(text='to_first_list', callback_data = 'to_first_list'))
	markup.add(types.InlineKeyboardButton(text='to_sec_list', callback_data = 'to_sec_list'))
	markup.add(types.InlineKeyboardButton(text='finish', callback_data = 'finish'))

	bot.edit_message_reply_markup(message.message.chat.id, message.message.message_id, "Главная", reply_markup = markup)
	@bot.callback_query_handler(func=lambda message: True)
	def pre_setting_list(message):
		settings_list(message)

def settings_return(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton(text= 'Всетаки я доверяю разрабу. Оставлю все как есть.', callback_data = 'return'))
	markup.add(types.InlineKeyboardButton(text='Я передумал передумывать.', callback_data = 'back'))

	bot.edit_message_reply_markup(message.message.chat.id, message.message.message_id, 'Перейдем к настройкам.', reply_markup = markup)
	@bot.callback_query_handler(func=lambda message: True)
	def pre_setting_list(message):
		settings_list(message)

def setting_first_list(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton(text='return', callback_data = 'return'))
	markup.add(types.InlineKeyboardButton(text='punkt_one_first_setting', callback_data = 'to_first_first_setting'))
	markup.add(types.InlineKeyboardButton(text='punkt_two_first_setting', callback_data = 'to_sec_first_setting'))
	markup.add(types.InlineKeyboardButton(text='finish', callback_data = 'finish'))
	markup.add(types.InlineKeyboardButton(text='back', callback_data = 'back'))
	
	bot.edit_message_reply_markup(message.message.chat.id, message.message.message_id, "Настройка №2", reply_markup = markup)
	@bot.callback_query_handler(func=lambda message: True)
	def pre_setting_list(message):
		settings_list(message)

def setting_sec_list(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton(text='return', callback_data = 'return'))
	markup.add(types.InlineKeyboardButton(text='punkt_one_sec_setting', callback_data = 'punkt_one_sec_setting'))
	markup.add(types.InlineKeyboardButton(text='punkt_two_sec_setting', callback_data = 'punkt_two_sec_setting'))
	markup.add(types.InlineKeyboardButton(text='finish', callback_data = 'finish'))
	markup.add(types.InlineKeyboardButton(text='back', callback_data = 'back'))

	bot.edit_message_reply_markup(message.message.chat.id, message.message.message_id, "Настройка №3", reply_markup = markup)
	@bot.callback_query_handler(func=lambda message: True)
	def pre_setting_list(message):
		settings_list(message)

def setting_finish(message):
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	markup.add('Да', 'Нет')

	end_settings = bot.send_message(message.from_user.id, "Вы закночили?", reply_markup = markup)
	bot.register_next_step_handler(end_settings, finish_reg)

def sign(message):
	bot.send_message(message.chat.id, 'Вход пожилой!', reply_markup = types.ReplyKeyboardRemove(selective=False))

			