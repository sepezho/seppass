from telebot import types
from login import login_pass_query

def settings_begin_mess(message, bot_old):
	global bot
	bot = bot_old
	bot.send_message(message.chat.id, 'Начнем с настроек.')
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
		return
	if message.data == 'store_keys':
		setting_store_keys(message)
		return
	if message.data == 'store_pass':
		setting_store_pass(message)
		return
	if message.data == 'auth':
		setting_authentication(message)
		return
	if message.data == 'finish':
		setting_finish(message.message.chat.id)
		return
	if message.data == 'back':
		settings_main(message)
		return
	if message.data == 'key_serv':
		#  or message.data == 'key_on_GitHub'
		settings["store_keys"] = message.data
		return
	if message.data == 'pass_server' or message.data == 'pass_user':
		#  or message.data == 'pass_on_activiti'
		settings["store_pass"] = message.data
		return
	if message.data == 'tg_auth':
		#  or message.data == 'device_auth' or message.data == 'pass_auth' or message.data == 'mail_auth'
		settings["auth"] = message.data
		return

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
	# markup.add(types.InlineKeyboardButton(text='GitHub (dont work)', callback_data = 'key_on_GitHub'))
	markup.add(types.InlineKeyboardButton(text='Вернуться', callback_data = 'back'))
	markup.add(types.InlineKeyboardButton(text='Закончить', callback_data = 'finish'))
	
	bot.edit_message_reply_markup(message.message.chat.id, message.message.message_id, "", reply_markup = markup)
	@bot.callback_query_handler(func=lambda message: True)
	def pre_setting_list(message):
		settings_list(message)

def setting_store_pass(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton(text='На сервере (файликом)', callback_data = 'pass_server'))
	markup.add(types.InlineKeyboardButton(text='Вводить каждую новую сессию', callback_data = 'pass_user'))
	# markup.add(types.InlineKeyboardButton(text='Вводить при каждой активности', callback_data = 'pass_on_activiti'))
	markup.add(types.InlineKeyboardButton(text='Вернуться', callback_data = 'back'))
	markup.add(types.InlineKeyboardButton(text='Закончить', callback_data = 'finish'))
	
	bot.edit_message_reply_markup(message.message.chat.id, message.message.message_id, "", reply_markup = markup)
	@bot.callback_query_handler(func=lambda message: True)
	def pre_setting_list(message):
		settings_list(message)

def setting_authentication(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton(text='Через аккаунт телеграм', callback_data = 'tg_auth'))
	# markup.add(types.InlineKeyboardButton(text='Через устройство', callback_data = 'device_auth'))
	# markup.add(types.InlineKeyboardButton(text='По паролю', callback_data = 'pass_auth'))
	# markup.add(types.InlineKeyboardButton(text='Mail (dont work)', callback_data = 'mail_auth'))
	markup.add(types.InlineKeyboardButton(text='Вернуться', callback_data = 'back'))
	markup.add(types.InlineKeyboardButton(text='Закончить', callback_data = 'finish'))

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
	bot.delete_message(message.chat.id, message.message_id)
	bot.delete_message(message.chat.id, message.message_id - 1)
	bot.delete_message(message.chat.id, message.message_id - 2)

	if message.text == 'Да':
		login_pass_query(message, bot, settings)
	elif message.text == 'Нет':
		settings_begin(message)
	else:
		bot.send_message(message.chat.id, "Я вас не понял.")
		setting_finish(message.chat.id)
