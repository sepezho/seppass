import os
import gnupg
def insert_main(message, bot_old, password):
	global bot
	bot = bot_old
	command = message.text.split()
	global name
	name = command[1]
	if len(command) == 2:
		if os.path.isfile('/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) +'/'+ name+'.gpg'):
			bot.send_message(message.chat.id, 'Такая запись уже существует.')
		else:
			msg = bot.send_message(message.chat.id,'Отправте свою запись (не бойтесь, за ее сохранность, я ее удалю из ваших сообщений).')
			bot.register_next_step_handler(msg, insert_pass_query)
	else:
		bot.send_message(message.chat.id,'Используйте правильный синтаксис: /insert папка/имя_записи')
		return
def insert_pass_query(message):
	part = name.split('/')
	val_old = '/'
	for val in part:
		if val not in part[-1]:
			val_old = val_old+val+'/'
			if not os.path.exists('/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) + val_old):
				os.mkdir('/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) + val_old)
	gpg = gnupg.GPG(gnupghome='/home/sepezho/.gnupg/')
	encrypted_data = gpg.encrypt(message.text, str(message.from_user.id))
	with open('/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) + '/' + name + '.gpg', 'w') as f:
		f.write(str(encrypted_data))

	bot.send_message(message.chat.id,'Запись ' + name + ' добавлена.')
