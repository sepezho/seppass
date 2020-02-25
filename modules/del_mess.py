import time

def del_mess(message, bot, num):
	print('delete')
	# time.sleep(5)
	# for i in range(num):
	# 	bot.delete_message(message.chat.id, message.message_id - i)

# def del_mess_main(message, bot):
# 	bot.send_message(message.chat.id, 'Введите кол-во сообщений, которые хотите удалить.')

# 	@bot.callback_query_handler(func=lambda message: True)
# 	def pre_del_mess(message):
# 		if int(message) >= 100:
# 			del_mess(message, bot, int(message))
# 		else:
# 			bot.send_message(message.chat.id, 'Удалить можно не больше 100 сообщений за раз.')