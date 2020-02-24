import gnupg
import os
from del_mess import del_mess

def cat_main(message, bot, password):
	# if message.text[-1] == ' ':
		# message.text = message.text[:-1]
		# print(message.text[:-1]+'a')
	command = message.text.split()
	if len(command) == 2:
		name = command[1]
		file = '/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) +'/'+ name+'.gpg'
		if os.path.isfile(file):
			gpg = gnupg.GPG()
			with open(file, 'rb') as f:
				# status = gpg.decrypt_file(file=f, passphrase=password)
				status = gpg.decrypt_file(file=f)
			os.system('echo RELOADAGENT | gpg-connect-agent')
			msg = bot.send_message(message.chat.id, 'Запись '+name+':\n\n'+str(status))
			del_mess(msg, bot, 2)
		else:
			msg = bot.send_message(message.chat.id, 'Такой записи не существует.')
			del_mess(msg, bot, 2)
	else:
		msg = bot.send_message(message.chat.id,'Используйте правильный синтаксис: /cat папка/имя_записи')
		del_mess(msg, bot, 2)
