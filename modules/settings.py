from os import path
from os import remove
from sqlite3 import connect
from telebot import types
from login import login_pass_query
from del_mess import del_mess

def settings_begin_mess(message, bot_old, is_auth_import, password_old):
	global bot
	global is_auth
	global password
	bot = bot_old
	is_auth = is_auth_import
	password = password_old

	msg = bot.send_message(message.chat.id, 'Перейдем к настройкам.')
	settings_begin(message)


def settings_begin(message):
	global settings
	settings = {
		"store_pass": "pass_user",
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

	elif message.data == 'store_pass':
		setting_store_pass(message)

	elif message.data == 'finish':
		# here was an issue, and i fixed it, by using shitty method
		json = message.message.json
		setting_finish(json['chat']['id'])

	elif message.data == 'back':
		settings_main(message)

	elif message.data == 'pass_server' or message.data == 'pass_user':
		settings["store_pass"] = message.data


def settings_return(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton(text= 'Все-таки я доверяю разрабу. Оставлю все как есть.', callback_data = 'finish'))
	markup.add(types.InlineKeyboardButton(text='Я передумал передумывать.', callback_data = 'back'))
	bot.edit_message_reply_markup(message.message.json.chat.id, message.message.message_id, 'Вернемся к настройкам.', reply_markup = markup)
	@bot.callback_query_handler(func=lambda message: True)
	def pre_setting_list(message):
		settings_list(message)


def settings_main(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton(text='Хранение пароля', callback_data = 'store_pass'))
	markup.add(types.InlineKeyboardButton(text='Вернуться', callback_data = 'return'))
	markup.add(types.InlineKeyboardButton(text='Закончить', callback_data = 'finish'))
	bot.edit_message_reply_markup(message.message.json.chat.id, message.message.message_id, "", reply_markup = markup)
	@bot.callback_query_handler(func=lambda message: True)
	def pre_setting_list(message):
		settings_list(message)


def setting_store_pass(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton(text='На сервере (файликом)', callback_data = 'pass_server'))
	markup.add(types.InlineKeyboardButton(text='Вводить каждую новую сессию', callback_data = 'pass_user'))
	markup.add(types.InlineKeyboardButton(text='Вернуться', callback_data = 'back'))
	bot.edit_message_reply_markup(message.message.json.chat.id, message.message.message_id, "", reply_markup = markup)
	@bot.callback_query_handler(func=lambda message: True)
	def pre_setting_list(message):
		settings_list(message)


def setting_finish(chat_id):
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	markup.add('Да')
	markup.add('Нет')
	msg_handler = bot.send_message(chat_id, "Вы закночили?", reply_markup = markup)
	bot.register_next_step_handler(msg_handler, finish_reg)


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
		bot.send_message(message.chat.id, "Отмена.")
		for i in range(5):
			bot.delete_message(message.chat.id, message.message_id - i)
		return


def finish_settings_auth(message):
	try:
		conn = connect('DataBase.db', check_same_thread=False)
		c = conn.cursor()
		query = "UPDATE Users SET Settings = \""+str(settings)+"\" WHERE User_id = 'user_"+str(message.chat.id)+"'"
		c.execute(query)
		conn.commit()
		conn.close()

	except:
		msg = bot.send_message(message.chat.id, 'Произошла ошибка.')
		del_mess(msg, bot, 2)
		return

	try:
		if settings["store_pass"] == "pass_server":
			with open('/Seppass/Users_folder/user_' + str(message.chat.id) + '/user_data/Nothing.txt', 'w') as f:
				f.write(password)

		else:
			if path.isfile('/Seppass/Users_folder/user_' + str(message.chat.id) + '/user_data/Nothing.txt'):
				remove('/Seppass/Users_folder/user_' + str(message.chat.id) + '/user_data/Nothing.txt')
	except:
		msg = bot.send_message(message.chat.id, 'Произошла ошибка.')
		del_mess(msg, bot, 2)
		return
