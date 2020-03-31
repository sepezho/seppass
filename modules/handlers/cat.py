import os
import gnupg
from del_mess import del_mess


def cat_main(message, bot, password):
	command = message.text.split()
	msg = None
	name = command[1]
	file = '/home/sepezho/Documents/Seppass/Users_folder/user_' + str(message.from_user.id) +'/main/'+ name+'.gpg'

	if os.path.isfile(file):
		try:
			gpg = gnupg.GPG()

			with open(file, 'rb') as f:
				status = gpg.decrypt_file(file=f, passphrase=password)

			os.system('echo RELOADAGENT | gpg-connect-agent')
			msg = bot.send_message(message.chat.id, 'Запись '+name+':')
			
			if str(status) != '':
				msg = bot.send_message(message.chat.id, str(status))
				del_mess(msg, bot, 3)
				return
				
			else:
				msg = bot.send_message(message.chat.id, 'Undefined')
				del_mess(msg, bot, 3)
				return

		except TypeError as e:
			msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
			del_mess(msg, bot, 2)
			return
	else:
		msg = bot.send_message(message.chat.id, 'Такой записи не существует.')
		del_mess(msg, bot, 2)
		return
