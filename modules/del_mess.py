import time

message = None
num_old = None

def del_mess(message_old, bot, num_old):
	global message
	global num

	# time.sleep(30)
	if message != None:
		for i in range(num):
			try:
				bot.delete_message(message.chat.id, message.message_id - i)

			except TypeError as e:
				print('DELETE_ERROR')
				return

	num = num_old
	message = message_old