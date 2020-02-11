import os
import gnupg
def touch_main(message, bot_old):
	global bot
	bot = bot_old
	command = message.text.split()
	global way
	way = '/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id)
	if (len(command) == 2) and (command[1].find('//') == -1) and (command[1].find('.') == -1) and (command[1][-1] != '/'):
		global name
		name = command[1]
		if os.path.isfile(way +'/'+ name+'.gpg'):
			bot.send_message(message.chat.id, 'Такая запись уже существует.')
		else:
			part = name.split('/')
			print(len(part))
			if len(part) < 9:
				msg = bot.send_message(message.chat.id,'Отправте свою запись (не бойтесь, за ее сохранность, я ее удалю из ваших сообщений).')
				try:
					bot.register_next_step_handler(msg, touch_pass_query)
				except:
					bot.send_message(message.chat.id,'Произошла ошибка. Вы уверенны, что назвали путь правильно?')
			else:
				bot.send_message(message.chat.id,'Вы хотите создать очень много папок. Макс. глубина - 7 папок. Зачем вам столько -.-')
	else:
		bot.send_message(message.chat.id,'Используйте правильный синтаксис: /touch папка/имя_записи')
		return
def touch_pass_query(message):
	val_old = '/'
	part = name.split('/')
	for val in part:
		if val not in part[-1]:
			val_old = val_old+val+'/'
			if not os.path.exists(way + val_old):
				os.mkdir(way + val_old)
	gpg = gnupg.GPG(gnupghome='/home/sepezho/.gnupg/')
	encrypted_data = gpg.encrypt(message.text, str(message.from_user.id))
	with open(way + '/' + name + '.gpg', 'w') as f:
		f.write(str(encrypted_data))
	bot.send_message(message.chat.id,'Запись ' + name + ' добавлена.')
