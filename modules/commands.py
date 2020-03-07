import sys
from auth import auth_main
from del_mess import del_mess

sys.path.append('./modules/handlers')
from touch import touch_main
from mkd import mkd_main
from cat import cat_main
from ls import ls_main
from rm import rm_main
from mv import mv_main
from gen import gen_main
from edit import edit_main
from getgit import getgit
from settings import settings_begin_mess
from delete_account import delete_account_main

user_password = None


def commands_main(bot):
	@bot.message_handler(commands=['auth'])
	def message_handler_auth_main(message):
		global user_password
		if user_password != None:
			msg = bot.send_message(message.chat.id, 'Вы уже аутентифицировались.')
			del_mess(msg, bot, 2)
		else:
			user_password = auth_main(message, bot)

	@bot.message_handler(commands=['touch'])
	def touch_func_in_main(message):
		global user_password
		if user_password != None:
			touch_main(message, bot)
		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)

	@bot.message_handler(commands=['logout'])
	def logout_func_in_main(message):
		global user_password
		if user_password != None:
			user_password = None
			msg = bot.send_message(message.chat.id, 'Вы вышли.')
			del_mess(msg, bot, 2)
		else:
			msg = bot.send_message(message.chat.id, 'Чтобы выйти, надо войти, используя /auht.\n\n(с) Конфуций.')
			del_mess(msg, bot, 2)

	@bot.message_handler(commands=['mkd'])
	def mkd_handler_auth_main(message):
		global user_password
		if user_password != None:
			mkd_main(message, bot)
		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)

	@bot.message_handler(commands=['cat'])
	def cat_func_in_main(message):
		global user_password
		if user_password != None:
			cat_main(message, bot, user_password)
		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)

	@bot.message_handler(commands=['ls'])
	def ls_func_in_main(message):
		global user_password
		if user_password != None:
			ls_main(message, bot)
		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)

	@bot.message_handler(commands=['rm'])
	def rm_func_in_main(message):
		global user_password
		if user_password != None:
			rm_main(message, bot)
		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)

	@bot.message_handler(commands=['mv'])
	def mv_handler_auth_main(message):
		global user_password
		if user_password != None:
			mv_main(message, bot)
		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)

	@bot.message_handler(commands=['gen'])
	def gen_handler_auth_main(message):
		global user_password
		if user_password != None:
			gen_main(message, bot)
		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)
	
	@bot.message_handler(commands=['edit'])
	def edit_handler_auth_main(message):
		global user_password
		if user_password != None:
			edit_main(message, bot)
		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)

	@bot.message_handler(commands=['delete_account'])
	def delete_account_handler_auth_main(message):
		global user_password
		if user_password != None:
			user_password = delete_account_main(message, bot, user_password)
		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)

	@bot.message_handler(commands=['getgit'])
	def connect_to_git_handler_auth_main(message):
		global user_password
		if user_password != None:
			getgit(message, bot)
		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)

	# @bot.message_handler(commands=['delmes'])
	# def del_mess_handler_auth_main(message):
	# 	global user_password
	# 	if user_password != None:
	# 		del_mess_main(message, bot)
	# 	else:
	# 		msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
	# 		del_mess(msg, bot, 2)
	
	@bot.message_handler(commands=['settings'])
	def settings_handler_auth_main(message):
		global user_password
		if user_password != None:
			settings_begin_mess(message, bot, True, user_password)
		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)
	
	@bot.message_handler(func=lambda message: True, content_types=['text'])
	def error(message):
		msg = None
		if message.text[0] != '/':
			msg = bot.send_message(message.chat.id,'Я смотрю ты потерялся. Используй /help.')
		else:
			msg = bot.send_message(message.chat.id,'Функции '+message.text+' не существует. Используй /help.')
		del_mess(msg, bot, 2)
