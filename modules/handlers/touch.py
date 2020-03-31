from os import path
from os import makedirs
from gnupg import GPG
from del_mess import del_mess


def touch_main(message, bot):
	command = message.text.split()
	way = '/home/sepezho/Documents/Seppass/Users_folder/user_' + str(message.from_user.id)+'/main'
	
	name = command[1]
	if not path.isfile(way +'/'+ name+'.gpg'):
		if not path.isdir(way +'/'+ name):
			if len(name.split('/')) < 9:
				msg_handler = bot.send_message(message.chat.id,'Отправте свою запись (не бойтесь, за ее сохранность, я ее удалю из ваших сообщений).')
				bot.register_next_step_handler(msg_handler, lambda msg: touch_pass_query(msg, bot, way, name))

			else:
				msg = bot.send_message(message.chat.id,'Вы хотите создать очень много папок. Макс. глубина - 7 папок. Зачем вам столько -.-')
				del_mess(msg, bot, 2)
				return
		else:
			msg = bot.send_message(message.chat.id,'Папка с таким названием уже сужествует в этой директории.')
			del_mess(msg, bot, 2)
			return
	else:
		msg = bot.send_message(message.chat.id,'Файл с таким названием в этой папке уже существует.')
		del_mess(msg, bot, 2)
		return


def touch_pass_query(message, bot, way, name):
	val_old = '/'
	part = name.split('/')
	
	try:
		if not path.isdir(way + '/' + '/'.join(part[:-1])):
			makedirs(way + '/'+'/'.join(part[:-1]))

		gpg = GPG()
		gpg.encrypt(
			message.text,
			recipients=['user_'+str(message.from_user.id)],
			output=way + '/' + name + '.gpg',
		)

		msg = bot.send_message(message.chat.id,'Запись ' + name + ' добавлена.')
		del_mess(msg, bot, 4)
		return

	except TypeError as e:
		msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
		del_mess(msg, bot, 4)
		return

