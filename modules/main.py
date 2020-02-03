def main(message, bot_old):
	global bot
	bot = bot_old
	bot.send_message(message.chat.id, 'Вы вошли.')

	# @bot.message_handler(commands=['ls'])
	# def message_handler_auth_main(message):
	# @bot.message_handler(commands=['cat'])
	# def message_handler_auth_main(message):
	# @bot.message_handler(commands=['insert'])
	# def message_handler_auth_main(message):
	# @bot.message_handler(commands=['generate'])
	# def message_handler_auth_main(message):
	# @bot.message_handler(commands=['edit'])
	# def message_handler_auth_main(message):
	# @bot.message_handler(commands=['rm'])
	# def message_handler_auth_main(message):
	# @bot.message_handler(commands=['mv'])
	# def message_handler_auth_main(message):
	# @bot.message_handler(commands=['settings'])
	# def message_handler_auth_main(message):
