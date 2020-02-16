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
		
def touch_pass_query(message):
	val_old = '/'
	part = name.split('/')
	if not os.path.isdir(way + '/' + '/'.join(part[:-1])):
		os.makedirs(way + '/'+'/'.join(part[:-1]))
	gpg = gnupg.GPG()
	gpg.encrypt(
        message.text,
        # recipients=['user_'+user_id],
        recipients='sepezho',
        output=way + '/' + name + '.gpg',
    )
	bot.send_message(message.chat.id,'Запись ' + name + ' добавлена.')
