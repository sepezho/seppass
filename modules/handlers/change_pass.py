# from gnupg import GPG
# from os import system
# from sqlite3 import connect
from del_mess import del_mess

def change_pass_main(message, bot):
	try:

		# conn = connect('DataBase.db', check_same_thread=False)
		# c = conn.cursor()
		# query = "SELECT Key FROM Users WHERE User_id = 'user_"+str(message.from_user.id)+"'"
		# key = c.execute(query).fetchall()[0][0]

		# conn.commit()
		# conn.close()

		# # gpg = GPG()

		# print('---------')

		# system('gpg --edit-key '+key+' ; passwd '+' ; pass ; '+'123'+' ; save ; '+'Q')
		# # system('echo RELOADAGENT | gpg-connect-agent')
		# # system('echo RELOADAGENT | gpg-connect-agent')
		# system('echo RELOADAGENT | gpg-connect-agent')

		msg = bot.send_message(message.chat.id, 'Функция не работает, извините.')
		del_mess(msg, bot, 2)
		return

	except:
		msg = bot.send_message(message.chat.id, 'Произошла ошибка.')
		del_mess(msg, bot, 2)
		return