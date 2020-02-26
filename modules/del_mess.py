import time


def del_mess(message, bot, num):
	# print('dell_mes')
	time.sleep(5)
	for i in range(num):
		bot.delete_message(message.chat.id, message.message_id - i)
	return