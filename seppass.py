import telebot
import sys
from telebot import types

sys.path.append('./modules')
from auth import auth_main

url = "socks5://sockduser:f2%kE%.)as!S@46.101.118.222:6666"
telebot.apihelper.proxy = {
	'http': url,
	'https': url
}

bot = telebot.TeleBot("1028700604:AAHqqv3JQSvkmUubsjS442EFpUMUULKmPYg")

@bot.message_handler(commands=['start'])
def message_handler_start_main(message):
	bot.send_message(message.chat.id,
		'Привет!\nЯ - бот, предназначенный для хранения паролей. Хранение оных очень надежно, т.к. каждый шифруется вашим собственный'+
		' GPG ключем, пароль от которого знаете только вы (конечно если выбрали пункт "хранить пароль у себя" в настройках).'+
		'\n\nИспользуйте /auth, чтобы войти в акк, или создать его. Используйте команду /help, если растерялись.\n\nУдачи.'
		)

# isAuth = True
# @bot.message_handler(func=lambda message: isAuth, content_types=['text'])
# def message_handler_auth_main(message):
# 	bot.send_message(message.chat.id,'aa')
# 	return
@bot.message_handler(commands=['auth'])
def message_handler_auth_main(message):
	print(str(auth_main(message, bot)))

def main_handlers(message, password):
	bot.send_message(message.chat.id, 'Вы аутентифицировались.')

	@bot.message_handler(commands=['touch'])
	def touch_func_in_main(message):
		touch_main(message, bot)
	@bot.message_handler(commands=['mkd'])
	def mkd_handler_auth_main(message):
		mkd_main(message, bot)
	@bot.message_handler(commands=['cat'])
	def cat_func_in_main(message):
		cat_main(message, bot, password)
	@bot.message_handler(commands=['ls'])
	def ls_func_in_main(message):
		ls_main(message, bot)
	@bot.message_handler(commands=['rm'])
	def rm_func_in_main(message):
		rm_main(message, bot)
	@bot.message_handler(commands=['mv'])
	def mv_handler_auth_main(message):
		mv_main(message, bot)
	@bot.message_handler(commands=['gen'])
	def gen_handler_auth_main(message):
		gen_main(message, bot)
	@bot.message_handler(commands=['edit'])
	def edit_handler_auth_main(message):
		edit_main(message, bot)
	@bot.message_handler(commands=['settings'])
	def settings_handler_auth_main(message):
		settings.settings_begin_mess(message, bot, True, password)

	@bot.message_handler(func=lambda message: True, content_types=['text'])
	def error(message):
		if message.text[0] != '/':
			bot.send_message(message.chat.id,'Я смотрю ты потерялся. Используй /help.')
		else:
			bot.send_message(message.chat.id,'Функции '+message.text+' не существует. Используй /help.')
	


# @bot.message_handler(func=lambda message: isAuth, content_types=['text'])
# def message_handler_auth_main(message):


# def error_user_write():
# 	@bot.message_handler(func=lambda message: True, content_types=['text'])
# 	def error(message):
# 		auth_main(message, bot)
# 		return
# 	return

# error_user_write()

@bot.message_handler(commands=['help'])
def message_handler_auth_main(message):
	bot.send_message(message.chat.id,
	'Команды и их описание, которые может выполнять этот бот.\n\n'+
	'╠═══════════════════════════════╣\n'+
	'  Команды, доступные без авторизации:\n'+
	'╠═══════════════════════════════╣\n\n'+
	'/start - Приветствие, и небольшое описание возможностей бота.\n\n'+
	'/auth - Авторизация пользователя, для дальнейшей работы.\n\n'+
	'/about - О разработчике.\n\n'+
	'/help - Очень трудно догадаться (выводит это сообщение).\n\n'+
	'╠═══════════════════════════════╣\n'+
	'  Команды, доступные после авторизации:\n'+
	'╠═══════════════════════════════╣\n\n'+
	'/ls - Просмотр списка шифрованых записей. Используйте так: /ls папка/папка (или просто /ls)\n\n'+
	'/cat - Просмотр записи, но нужно ввести пароль, чтоб ее расшифровать.\nИспользуется так: /cat папка/имя_записи (после ввода пароля (если надо) вам вернется запись, которую вы шифровали с именем "name")\n\n'+
	'/touch - Создать новую запись, ввести ее сообщением.\nИспользуется так: /touch папка/имя_записи. После введите запись.\n\n'+
	'/mkd - Создать новую пустую папку.\nИспользуется так: /mkd папка/папка.\n\n'+
	'/gen - Сгенерирует запись, используя случайные буквы, цифры и спец. символы.\nИспользуйте так: /gen name -12 (Сгенерирует случаную запись с названием "name", длиной в 12 символов)\n\n'+
	'/edit - Изменяет запись.\nИспользуется так: /edit папка/имя_записи.\n\n'+
	'/rm - Удаляет запись.\nИспользуется так: /rm папка/имя_записи.\n\n'+
	'/mv - Перемещает запись.\nИспользуется так: /mv начальная_папка/имя_записи конечная_папка/имя_записи.\n\n'+
	'/settings - Настройки.'
	# '* - значит функция еще не готова или временно не работает. Мои извинения за неудобства.'
	)

@bot.message_handler(commands=['about'])
def message_handler_auth_main(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton(text= 'Сайт разработчика.', url='https://sepezho.ru'))

	bot.send_message(message.chat.id,
		'════════╣ Created by SEPEZHO ╠════════\n'+
		'Btw by this guy: Vladislav Bliznyuk\n'+
		'Start creating: 23.01.2020\n'+
		'End creating: __.__.____\n'+
		'Version: 0.0.1\n'+
		'Have a nice day\n'+
		'════════╣ Created by SEPEZHO ╠════════\n',
		reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
