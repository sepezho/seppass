from sys import path

from del_mess import del_mess
from command_checker import command_checker

path.append('/Seppass/modules/handlers')
path.append('/Seppass/modules/git')
from auth import auth_main
from settings import settings_begin_mess
from change_pass import change_pass_main
from delete_account import delete_account_main
from download_data import download_data_main
from rm_all import rm_all_main
from rm import rm_main
from touch import touch_main
from mkd import mkd_main
from cat import cat_main
from ls import ls_main
from mv import mv_main
from gen import gen_main
from edit import edit_main
# from git_gen_ssh import git_gen_ssh_main
from git_token import git_token_main
from git_init import git_init_main
from git_clone import git_clone_main
from git_push import git_push_main
from git_pull import git_pull_main

user_password = None


def commands_main(bot):
	@bot.message_handler(commands=['auth'])
	def auth_handler_main(message):
		global user_password
		if user_password != None:
			msg = bot.send_message(message.chat.id, 'Вы уже аутентифицировались.')
			del_mess(msg, bot, 2)

		else:
			if command_checker(message.text, 1, False):
				user_password = auth_main(message, bot)

			else:
				msg = bot.send_message(message.chat.id, 'Я не перевариваю все кроме латиницы цифр и пробелов а еще знака "/". Если в строке есть посторонние символы, тогда убери их >:(\nИспользуйте правильный синтаксис: /auth')
				del_mess(msg, bot, 2)

	@bot.message_handler(commands=['logout'])
	def logout_handler_main(message):
		global user_password
		if user_password != None:
			if command_checker(message.text, 1, False):
				user_password = None
				msg = bot.send_message(message.chat.id, 'Вы вышли.')
				del_mess(msg, bot, 2)

			else:
				msg = bot.send_message(message.chat.id, 'Я не перевариваю все кроме латиницы цифр и пробелов а еще знака "/". Если в строке есть посторонние символы, тогда убери их >:(\nИспользуйте правильный синтаксис: /logout')
				del_mess(msg, bot, 2)

		else:
			msg = bot.send_message(message.chat.id, 'Чтобы выйти, надо войти, используя /auht.\n\n(с) Конфуций.')
			del_mess(msg, bot, 2)

	@bot.message_handler(commands=['settings'])
	def settings_handler_main(message):
		global user_password
		if user_password != None:
			if command_checker(message.text, 1, False):
				settings_begin_mess(message, bot, True, user_password)

			else:
				msg = bot.send_message(message.chat.id, 'Я не перевариваю все кроме латиницы цифр и пробелов а еще знака "/". Если в строке есть посторонние символы, тогда убери их >:(\nИспользуйте правильный синтаксис: /settings')
				del_mess(msg, bot, 2)

		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)

	@bot.message_handler(commands=['changepass'])
	def change_pass_main_handler_main(message):
		global user_password
		if user_password != None:
			if command_checker(message.text, 1, False):
				change_pass_main(message, bot)

			else:
				msg = bot.send_message(message.chat.id, 'Я не перевариваю все кроме латиницы цифр и пробелов а еще знака "/". Если в строке есть посторонние символы, тогда убери их >:(\nИспользуйте правильный синтаксис: /changepass')
				del_mess(msg, bot, 2)

		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)

	@bot.message_handler(commands=['deleteacc'])
	def delete_account_handler_main(message):
		global user_password
		if user_password != None:
			if command_checker(message.text, 1, False):
				user_password = delete_account_main(message, bot, user_password)

			else:
				msg = bot.send_message(message.chat.id, 'Я не перевариваю все кроме латиницы цифр и пробелов а еще знака "/". Если в строке есть посторонние символы, тогда убери их >:(\nИспользуйте правильный синтаксис: /deleteacc')
				del_mess(msg, bot, 2)

		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)

	@bot.message_handler(commands=['downloaddata'])
	def download_data_main_rep_handler_main(message):
		global user_password
		if user_password != None:
			if command_checker(message.text, 1, False):
				download_data_main(message, bot)

			else:
				msg = bot.send_message(message.chat.id, 'Я не перевариваю все кроме латиницы цифр и пробелов а еще знака "/". Если в строке есть посторонние символы, тогда убери их >:(\nИспользуйте правильный синтаксис: /downloaddata')
				del_mess(msg, bot, 2)

		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)

	@bot.message_handler(commands=['rmall'])
	def rm_all_main_handler_main(message):
		global user_password
		if user_password != None:
			if command_checker(message.text, 1, False):
				rm_all_main(message, bot)

			else:
				msg = bot.send_message(message.chat.id, 'Я не перевариваю все кроме латиницы цифр и пробелов а еще знака "/". Если в строке есть посторонние символы, тогда убери их >:(\nИспользуйте правильный синтаксис: /rmall')
				del_mess(msg, bot, 2)

		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)

	@bot.message_handler(commands=['rm'])
	def rm_handler_main(message):
		global user_password
		if user_password != None:
			if command_checker(message.text, 2, False):
				rm_main(message, bot)

			else:
				msg = bot.send_message(message.chat.id, 'Я не перевариваю все кроме латиницы цифр и пробелов а еще знака "/". Если в строке есть посторонние символы, тогда убери их >:(\nИспользуйте правильный синтаксис: /rm папка/имя_записи\n\n(или /rm папка/папка)')
				del_mess(msg, bot, 2)

		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)

	@bot.message_handler(commands=['touch'])
	def touch_handler_main(message):
		global user_password
		if user_password != None:
			if command_checker(message.text, 2, False):
				touch_main(message, bot)

			else:
				msg = bot.send_message(message.chat.id, 'Я не перевариваю все кроме латиницы цифр и пробелов а еще знака "/". Если в строке есть посторонние символы, тогда убери их >:(\nИспользуйте правильный синтаксис: /touch папка/имя_записи')
				del_mess(msg, bot, 2)

		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)

	@bot.message_handler(commands=['mkd'])
	def mkd_handler_main(message):
		global user_password
		if user_password != None:
			if command_checker(message.text, 2, False):
				mkd_main(message, bot)

			else:
				msg = bot.send_message(message.chat.id, 'Я не перевариваю все кроме латиницы цифр и пробелов а еще знака "/". Если в строке есть посторонние символы, тогда убери их >:(\nИспользуйте правильный синтаксис: /mkd папка/папка')
				del_mess(msg, bot, 2)

		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)

	@bot.message_handler(commands=['cat'])
	def cat_handler_main(message):
		global user_password
		if user_password != None:
			if command_checker(message.text, 2, False):
				cat_main(message, bot, user_password)

			else:
				msg = bot.send_message(message.chat.id, 'Я не перевариваю все кроме латиницы цифр и пробелов а еще знака "/". Если в строке есть посторонние символы, тогда убери их >:(\nИспользуйте правильный синтаксис: /cat папка/имя_записи')
				del_mess(msg, bot, 2)

		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)

	@bot.message_handler(commands=['ls'])
	def ls_handler_main(message):
		global user_password
		if user_password != None:
			if command_checker(message.text, 2, True):
				ls_main(message, bot)

			else:
				msg = bot.send_message(message.chat.id, 'Я не перевариваю все кроме латиницы цифр и пробелов а еще знака "/". Если в строке есть посторонние символы, тогда убери их >:(\nИспользуйте правильный синтаксис: /ls папка/папка\n\n(или просто /ls)')
				del_mess(msg, bot, 2)

		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)

	@bot.message_handler(commands=['mv'])
	def mv_handler_main(message):
		global user_password
		if user_password != None:
			if command_checker(message.text, 3, False):
				mv_main(message, bot)

			else:
				msg = bot.send_message(message.chat.id, 'Я не перевариваю все кроме латиницы цифр и пробелов а еще знака "/". Если в строке есть посторонние символы, тогда убери их >:(\nИспользуйте правильный синтаксис: /mv начальный_путь конечный_путь\n\n(начальный путь указывается с названием перемещаемого папки/файла, конеченый путь - без)')
				del_mess(msg, bot, 2)

		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)

	@bot.message_handler(commands=['gen'])
	def gen_handler_main(message):
		global user_password
		if user_password != None:
			if command_checker(message.text, 4, False):
				gen_main(message, bot)

			else:
				msg = bot.send_message(message.chat.id, 'Я не перевариваю все кроме латиницы цифр и пробелов а еще знака "/". Если в строке есть посторонние символы, тогда убери их >:(\nИспользуйте правильный синтаксис: /gen папка/имя_записи длина_строки сложность_строки\n\n(Длина_строки - это число от 0 до 25;\nСложность_строки - это число от 0 до 2 (где 2 - это сложная строка))')
				del_mess(msg, bot, 2)

		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)

	@bot.message_handler(commands=['edit'])
	def edit_handler_main(message):
		global user_password
		if user_password != None:
			if command_checker(message.text, 2, False):
				edit_main(message, bot)

			else:
				msg = bot.send_message(message.chat.id, 'Я не перевариваю все кроме латиницы цифр и пробелов а еще знака "/". Если в строке есть посторонние символы, тогда убери их >:(\nИспользуйте правильный синтаксис: /edit папка/имя_записи')
				del_mess(msg, bot, 2)

		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)

	# @bot.message_handler(commands=['gitgenssh'])
	# def git_gen_ssh_handler_main(message):
	# 	global user_password
	# 	if user_password != None:
	# 		if command_checker(message.text, 1, False):
	# 			git_gen_ssh_main(message, bot)
	#
	# 		else:
	# 			msg = bot.send_message(message.chat.id, 'Я не перевариваю все кроме латиницы цифр и пробелов а еще знака "/". Если в строке есть посторонние символы, тогда убери их >:(\nИспользуйте правильный синтаксис: /gitgenssh')
	# 			del_mess(msg, bot, 2)
	#
	# 	else:
	# 		msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
	# 		del_mess(msg, bot, 2)

	@bot.message_handler(commands=['gittoken'])
	def git_token_handler_main(message):
		global user_password
		if user_password != None:
			if command_checker(message.text, 1, False):
				git_token_main(message, bot)

			else:
				msg = bot.send_message(message.chat.id, 'Я не перевариваю все кроме латиницы цифр и пробелов а еще знака "/". Если в строке есть посторонние символы, тогда убери их >:(\nИспользуйте правильный синтаксис: /gittoken')
				del_mess(msg, bot, 2)

		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)

	@bot.message_handler(commands=['gitinit'])
	def git_init_handler_main(message):
		global user_password
		if user_password != None:
			if command_checker(message.text, 1, False):
				git_init_main(message, bot)

			else:
				msg = bot.send_message(message.chat.id, 'Я не перевариваю все кроме латиницы цифр и пробелов а еще знака "/". Если в строке есть посторонние символы, тогда убери их >:(\nИспользуйте правильный синтаксис: /gitinit')
				del_mess(msg, bot, 2)

		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)

	@bot.message_handler(commands=['gitclone'])
	def git_clone_handler_main(message):
		global user_password
		if user_password != None:
			if command_checker(message.text, 1, False):
				git_clone_main(message, bot, user_password)

			else:
				msg = bot.send_message(message.chat.id, 'Я не перевариваю все кроме латиницы цифр и пробелов а еще знака "/". Если в строке есть посторонние символы, тогда убери их >:(\nИспользуйте правильный синтаксис: /gitclone')
				del_mess(msg, bot, 2)

		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)

	@bot.message_handler(commands=['gitpush'])
	def git_push_main_rep_handler_main(message):
		global user_password
		if user_password != None:
			if command_checker(message.text, 1, False):
				git_push_main(message, bot)

			else:
				msg = bot.send_message(message.chat.id, 'Я не перевариваю все кроме латиницы цифр и пробелов а еще знака "/". Если в строке есть посторонние символы, тогда убери их >:(\nИспользуйте правильный синтаксис: /gitpush')
				del_mess(msg, bot, 2)

		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)

	@bot.message_handler(commands=['gitpull'])
	def git_pull_main_rep_handler_main(message):
		global user_password
		if user_password != None:
			if command_checker(message.text, 1, False):
				git_pull_main(message, bot)

			else:
				msg = bot.send_message(message.chat.id, 'Я не перевариваю все кроме латиницы цифр и пробелов а еще знака "/". Если в строке есть посторонние символы, тогда убери их >:(\nИспользуйте правильный синтаксис: /gitpull')
				del_mess(msg, bot, 2)

		else:
			msg = bot.send_message(message.chat.id, 'Войдите, используя /auth')
			del_mess(msg, bot, 2)

	@bot.message_handler(func=lambda message: True, content_types=['text'])
	def error(message):
		if message.text[0] != '/':
			msg = bot.send_message(message.chat.id,'Я смотрю ты потерялся. Используй /help.')
			del_mess(msg, bot, 2)

		else:
			msg = bot.send_message(message.chat.id,'Функции '+message.text+' не существует. Используй /help.')
			del_mess(msg, bot, 2)
