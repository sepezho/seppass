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
def first_setting(message):
	print(first_setting)

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

	bot.send_message(message.chat.id, 'Перейдем к настройкам.')
	settings_main(message)


def settings_main(message):
	markup = types.InlineKeyboardMarkup()
	switch_button1 = types.InlineKeyboardButton(text='-', callback_data = '1')
	markup.add(switch_button1)
	switch_button2 = types.InlineKeyboardButton(text='2', callback_data = '2')
	markup.add(switch_button2)
	switch_button3 = types.InlineKeyboardButton(text='3', callback_data = '3')
	markup.add(switch_button3)
	
	# global first_setting
	first_setting = bot.send_message(message.chat.id, "Настройка №1", reply_markup = markup)
	bot.register_next_step_handler(first_setting, sec_setting_list)


@bot.callback_query_handler()
def sec_setting_list(message):
	print(message.data)
# def sec_setting_list(message):
# 	markup = types.InlineKeyboardMarkup()
# 	switch_button1 = types.InlineKeyboardButton(text='2', callback_data = '1')
# 	markup.add(switch_button1)
# 	switch_button2 = types.InlineKeyboardButton(text='2', callback_data = '2')
# 	markup.add(switch_button2)
# 	switch_button3 = types.InlineKeyboardButton(text='2', callback_data = '3')
# 	markup.add(switch_button3)
# 	switch_button3 = types.InlineKeyboardButton(text='back', callback_data = 'back')
# 	markup.add(switch_button3)
# 	sec_setting = bot.send_message(message.chat.id, "Настройка №2", reply_markup = markup)

# 	markup = types.InlineKeyboardMarkup()
# 	switch_button1 = types.InlineKeyboardButton(text='3', callback_data = '1')
# 	markup.add(switch_button1)
# 	switch_button2 = types.InlineKeyboardButton(text='3', callback_data = '2')
# 	markup.add(switch_button2)
# 	switch_button3 = types.InlineKeyboardButton(text='3', callback_data = '3')
# 	markup.add(switch_button3)
# 	switch_button_back = types.InlineKeyboardButton(text='back', callback_data = 'back')
# 	markup.add(switch_button_back)
# 	third_setting = bot.send_message(message.chat.id, "Настройка №3", reply_markup = markup)
	
# 	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
# 	markup.add('Да', 'Нет')
# 	end_settings = bot.send_message(message.chat.id, "Вы закночили?", reply_markup = markup)
	# bot.register_next_step_handler(end_settings, finish_reg)

# def finish_reg(message):
	# print(first_setting)


def sign(message):
	bot.send_message(message.chat.id, 'Вход пожилой!', reply_markup = types.ReplyKeyboardRemove(selective=False))
