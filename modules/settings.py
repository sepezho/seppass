import os
import sqlite3
from login import login_pass_query
from del_mess import del_mess
from telebot import types

def settings_begin_mess(message, bot_old, is_auth_import, password_old):
	global bot
	global is_auth
	global password
	bot = bot_old
	is_auth = is_auth_import
	password = password_old
	
	bot.send_message(message.chat.id, 'Перейдем к настройкам.')
	settings_begin(message)


def settings_begin(message):
	global settings
	settings = {
		"store_keys": "key_serv",
		"store_pass": "pass_user",
		"auth": "tg_auth"
	}

	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton(text= 'Я доверяю разрабу. Оставлю все как есть.', callback_data = 'finish'))
	markup.add(types.InlineKeyboardButton(text='Я гик. Все настрою сам.', callback_data = 'back'))
	
	bot.send_message(message.chat.id, '⚙️⚙️Настройки⚙️⚙️', reply_markup = markup)
	@bot.callback_query_handler(func=lambda message: True)
	def pre_setting_list(message):
		settings_list(message)


# ничего лучше не придумал ¯\_(ツ)_/¯


def settings_list(message):
	if message.data == 'return':
		settings_return(message)
	
	elif message.data == 'store_keys':
		setting_store_keys(message)
	
	elif message.data == 'store_pass':
		setting_store_pass(message)
	
	elif message.data == 'auth':
		setting_authentication(message)
	
	elif message.data == 'finish':
		setting_finish(message.message.chat.id)
	
	elif message.data == 'back':
		settings_main(message)
	
	elif message.data == 'key_serv':
		settings["store_keys"] = message.data
	
	elif message.data == 'pass_server' or message.data == 'pass_user':
		settings["store_pass"] = message.data
	
	elif message.data == 'tg_auth':
		settings["auth"] = message.data


def settings_return(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton(text= 'Все-таки я доверяю разрабу. Оставлю все как есть.', callback_data = 'finish'))
	markup.add(types.InlineKeyboardButton(text='Я передумал передумывать.', callback_data = 'back'))

	bot.edit_message_reply_markup(message.message.chat.id, message.message.message_id, 'Перейдем к настройкам.', reply_markup = markup)
	@bot.callback_query_handler(func=lambda message: True)
	def pre_setting_list(message):
		settings_list(message)


def settings_main(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton(text='Хранение ключей', callback_data = 'store_keys'))
	markup.add(types.InlineKeyboardButton(text='Хранение пароля', callback_data = 'store_pass'))
	markup.add(types.InlineKeyboardButton(text='Методы аутентификации', callback_data = 'auth'))
	markup.add(types.InlineKeyboardButton(text='Вернуться', callback_data = 'return'))
	markup.add(types.InlineKeyboardButton(text='Закончить', callback_data = 'finish'))

	bot.edit_message_reply_markup(message.message.chat.id, message.message.message_id, "", reply_markup = markup)
	@bot.callback_query_handler(func=lambda message: True)
	def pre_setting_list(message):
		settings_list(message)


def setting_store_keys(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton(text='На сервере', callback_data = 'key_serv'))
	markup.add(types.InlineKeyboardButton(text='Вернуться', callback_data = 'back'))
	
	bot.edit_message_reply_markup(message.message.chat.id, message.message.message_id, "", reply_markup = markup)
	@bot.callback_query_handler(func=lambda message: True)
	def pre_setting_list(message):
		settings_list(message)


def setting_store_pass(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton(text='На сервере (файликом)', callback_data = 'pass_server'))
	markup.add(types.InlineKeyboardButton(text='Вводить каждую новую сессию', callback_data = 'pass_user'))
	markup.add(types.InlineKeyboardButton(text='Вернуться', callback_data = 'back'))
	
	bot.edit_message_reply_markup(message.message.chat.id, message.message.message_id, "", reply_markup = markup)
	@bot.callback_query_handler(func=lambda message: True)
	def pre_setting_list(message):
		settings_list(message)


def setting_authentication(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton(text='Через аккаунт телеграм', callback_data = 'tg_auth'))
	markup.add(types.InlineKeyboardButton(text='Вернуться', callback_data = 'back'))

	bot.edit_message_reply_markup(message.message.chat.id, message.message.message_id, "", reply_markup = markup)
	@bot.callback_query_handler(func=lambda message: True)
	def pre_setting_list(message):
		settings_list(message)


def setting_finish(chat_id):
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	markup.add('Да')
	markup.add('Нет')

	end_settings = bot.send_message(chat_id, "Вы закночили?", reply_markup = markup)
	bot.register_next_step_handler(end_settings, finish_reg)


def finish_reg(message):
	if message.text == 'Да' and not is_auth:
		for i in range(3):
			bot.delete_message(message.chat.id, message.message_id - i)
		login_pass_query(message, bot, settings)
		
	elif message.text == 'Да' and is_auth:
		for i in range(5):
			bot.delete_message(message.chat.id, message.message_id - i)
		finish_settings_auth(message)

	elif message.text == 'Нет':
		settings_begin(message)
	
	else:
		bot.send_message(message.chat.id, "Я вас не понял.")
		setting_finish(message.chat.id)


def finish_settings_auth(message):
	try:
		conn = sqlite3.connect('DataBase.db', check_same_thread=False)
		c = conn.cursor()
		query = "UPDATE Users SET Settings = \""+str(settings)+"\" WHERE User_id = 'user_"+str(message.from_user.id)+"'"
		c.execute(query)
		conn.commit()
		conn.close()
	
	except TypeError as e:
		msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
		del_mess(msg, bot, 2)
		return
	
	try:
		if settings["store_pass"] == "pass_server":
			with open('/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) + '/Nothing.txt', 'w') as f:
				f.write(password)
		
		else:
			if os.path.isfile('/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) + '/Nothing.txt'):
				os.remove('/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) + '/Nothing.txt')
	except TypeError as e:
		msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
		del_mess(msg, bot, 2)
		return

