message_to_delete = None
num_to_delete = None

def del_mess(message, bot, num):
	global message_to_delete
	global num_to_delete

	if message_to_delete != None:
		for i in range(num_to_delete):
			try:
				bot.delete_message(message_to_delete.chat.id, message_to_delete.message_id - i)
			except:
				print('delete_error')
				
	message_to_delete = message
	num_to_delete = num