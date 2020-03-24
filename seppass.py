import telebot

from sys import path
path.append('./modules')
from commands import commands_main

proxy_url = "socks5://sockduser:f2%kE%.)as!S@46.101.118.222:6666"
telebot.apihelper.proxy = {
	'http': proxy_url,
	'https': proxy_url
}
bot = telebot.TeleBot("1028700604:AAHqqv3JQSvkmUubsjS442EFpUMUULKmPYg")


@bot.message_handler(commands=['start'])
def message_handler_start_main(message):
	bot.send_message(message.chat.id,
		'Привет!\nЯ - бот, предназначенный для хранения паролей. Хранение оных очень надежно, т.к. каждый шифруется вашим собственный'+
		' GPG ключем, пароль от которого знаете только вы (конечно если выбрали пункт "хранить пароль у себя" в настройках).'+
		'\n\nИспользуйте /auth, чтобы войти в акк, или создать его. Используйте команду /help, если растерялись.\n\nУдачи.'
		)
	return

@bot.message_handler(commands=['help'])
def message_handler_auth_main(message):
	bot.send_message(message.chat.id,
	'Команды и их описание, которые может выполнять этот бот.\n\n'+
	'╠═══════════════════════════╣\n'+
	'  Команды, доступные всегда:\n'+
	'╠═══════════════════════════╣\n\n'+
	'/start - Приветствие, и небольшое описание возможностей бота.\n\n'+
	'/auth - Авторизация пользователя, для дальнейшей работы.\n\n'+
	'/about - О разработчике.\n\n'+
	'/help - Очень трудно догадаться (выводит это сообщение).\n\n'+
	'╠═══════════════════════════╣\n'+
	'  Команды, доступные после авторизации:\n'+
	'╠═══════════════════════════╣\n\n'+
	'/ls - Просмотр списка шифрованых записей. \nИспользуйте так: /ls папка/папка (или просто /ls)\n\n'+
	'/cat - Просмотр записи, но нужно ввести пароль, чтоб ее расшифровать.\nИспользуйте так: /cat папка/имя_записи (после ввода пароля (если надо) вам вернется запись, которую вы шифровали с именем "name")\n\n'+
	'/touch - Создать новую запись, ввести ее сообщением.\nИспользуйте так: /touch папка/имя_записи. После введите запись.\n\n'+
	'/mkd - Создать новую пустую папку.\nИспользуйте так: /mkd папка/папка.\n\n'+
	'/gen - Сгенерирует запись, используя случайные буквы, цифры и спец. символы.\nИспользуйте так: /gen name -12 (Сгенерирует случаную запись с названием "name", длиной в 12 символов)\n\n'+
	'/edit - Изменяет запись.\nИспользуйте так: /edit папка/имя_записи.\n\n'+
	'/clearall - Удаляет все записи, даже скрытые файлы и папки в /main.\n\n'+
	'/rm - Удаляет запись.\nИспользуйте так: /rm папка/имя_записи ("/rm *" - для удаления всех видимых файлов и папкок) .\n\n'+
	'/mv - Перемещает запись.\nИспользуйте так: /mv начальная_папка/имя_записи конечная_папка/имя_записи.\n\n'+
	'/changepass - Смена пароля gpg ключа (соответственно и пароля для входа).\n\n'+
	'/logout - Выход из аккаунта.\n\n'+
	'/deleteacc - Удаление аккаунта. Но зачем? Не покидайте меня :c \n\n'+
	'/settings - Настройки.\n\n'+
	'╠═══════════════════════════╣\n'+
	'  Команды, связанные с git-ом:\n'+
	'╠═══════════════════════════╣\n\n'+
	'/gitgenssh - Генерация 4096-битного ssh ключа.\n\n'+
	'/gitpush - Загружает все изменения в папке на GitHub.\n\n'+
	'/gitpull - Скачивает все изменения с репозитория на GitHub, после подключения оного.\n\n'+
	'/gitinit - Инициализирует папку с записаями, и создает новую репу, для gitHub.\n\n'+
	'/gitclone - Клон репозитория с вашими записями на сервер !!ПОСЛЕ ПОДКЛЮЧЕНИЯ ПО SSH!!'
	)
	return


@bot.message_handler(commands=['about'])
def message_handler_auth_main(message):
	markup = telebot.types.InlineKeyboardMarkup()
	markup.add(telebot.types.InlineKeyboardButton(text= 'Сайт разработчика.', url='https://sepezho.ru'))
	bot.send_message(message.chat.id,
		'═══════╣ Created by SEPEZHO ╠═══════\n'+
		'Btw by this guy: Vladislav Bliznyuk\n'+
		'Start creating: 23.01.2020\n'+
		'End creating: __.__.____\n'+
		'Version: 0.0.1\n'+
		'Have a nice day\n'+
		'═══════╣ Created by SEPEZHO ╠═══════\n',
		reply_markup=markup)
	return


commands_main(bot)


bot.polling()