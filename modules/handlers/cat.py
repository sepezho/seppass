import gnupg
import os
def cat_main(message, bot_old, password):
	global bot
	bot = bot_old
	command = message.text.split()
	global name
	name = command[1]
	if len(command) == 2:
		if os.path.isfile('/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) +'/'+ name+'.gpg'):
			with open('/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) + '/' + name + '.gpg', 'r') as f:
				 text = f.read()
			gpg = gnupg.GPG(gnupghome='/home/sepezho/.gnupg/')
			data = gpg.decrypt(text, passphrase=password)
			bot.send_message(message.chat.id, data)
		else:
			bot.send_message(message.chat.id, 'Такой записи не существует.')
	else:
		bot.send_message(message.chat.id,'Используйте правильный синтаксис: /cat папка/имя_записи')
		return