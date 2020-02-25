import time


def del_mess(message, bot, num):
	time.sleep(10)
	for i in range(num):
		bot.delete_message(message.chat.id, message.message_id - i)