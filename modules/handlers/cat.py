import gnupg
import os

def cat_main(message, bot, password):
	command = message.text.split()
	name = command[1]
	if len(command) == 2:
		file = '/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) +'/'+ name+'.gpg'
		if os.path.isfile(file):
			gpg = gnupg.GPG()
			with open(file, 'rb') as f:
				# status = gpg.decrypt_file(file=f, passphrase=password)
				status = gpg.decrypt_file(file=f)
			os.system('echo RELOADAGENT | gpg-connect-agent')
			bot.send_message(message.chat.id, 'Запись '+name+':\n\n'+str(status))
		else:
			bot.send_message(message.chat.id, 'Такой записи не существует.')
	else:
		bot.send_message(message.chat.id,'Используйте правильный синтаксис: /cat папка/имя_записи')
