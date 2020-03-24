from gnupg import GPG
from del_mess import del_mess

def change_pass(message, bot):
	try:
		gpg = GPG()
		key_arr = gpg.search_keys('user_'+str(message.from_user.id), '<sepezho@desktop>')
		# key_arr = gpg.list_keys('user_'+str(message.from_user.id))
		print(str(key_arr))
		print('---------')
		print(key_arr[0].keyid)

		system('echo RELOADAGENT | gpg-connect-agent')

		msg = bot.send_message(message.chat.id, 'Я закончил.')
		del_mess(msg, bot, 2)
		return

	except TypeError as e:
		msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
		del_mess(msg, bot, 2)
		return