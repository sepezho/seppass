import os
import gnupg
import random
from telebot import types
from del_mess import del_mess


def gen_main(message, bot):
	global way
	global name
	command = message.text.split()
	way = '/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id)
	msg = None
	
	if (len(command) == 4) and (command[1].find('//') == -1) and (command[1].find('.') == -1) and (command[1][0] != '/') and (command[1][-1] != '/'):
		name = command[1]
		
		if os.path.isfile(way +'/'+ name+'.gpg'):
			msg = bot.send_message(message.chat.id,'Файл с таким названием в этой папке уже существует.\n\n')

		else:
			if os.path.isdir(way +'/'+ name):
				msg = bot.send_message(message.chat.id,'Папка с таким названием уже сужествует в этой директории.\n\n')
							
			else:
				part = name.split('/')
				if len(part) < 9:
					if int(command[2]) < 26:
						return generate_req(bot, command, message)

					else:
						msg = bot.send_message(message.chat.id,'Макс. длина генерации - 25 симболов.')

				else:
					msg = bot.send_message(message.chat.id,'Вы хотите создать очень много папок. Макс. глубина - 7 папок. Зачем вам столько -.-')

	else:
		msg = bot.send_message(message.chat.id,'Используйте правильный синтаксис: /gen папка/имя_записи 12 1')

	del_mess(msg, bot, 2)


def pass_gen(command):
	password = ''
	if int(command[3]) == 0:
		chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
	
	elif int(command[3]) == 1:
		chars = '+=_-)(*?:%;№"!,}{[]><.~`/|abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
	
	elif int(command[3]) == 2:
		chars = '+=_-)(*?:%;№"!,}{[]><.~`/|+=_-)(*?:%;№"!,}{[]><.~`/|abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
	
	else:
		msg = bot.send_message(message.chat.id,'Сложность пароля варьируется от 0 до 2.')
		del_mess(msg, bot, 2)
		return

	for i in range(int(command[2])):
		password += random.choice(chars)
	
	return password


num = 0
def generate_req(bot, command, message):
	global num
	num += 3

	def finish_gen(message):
		if message.text == 'Да':
			msg = bot.send_message(message.chat.id,'Запись '+name+' сохранена.', reply_markup = types.ReplyKeyboardRemove(selective=False))
			del_mess(msg, bot, num+1)
			
			try:
				gen_pass_query(password, str(message.from_user.id))
			
			except TypeError as e:
				msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
				del_mess(msg, bot, num+2)
				return

		elif message.text == 'Создать новую':
			bot.send_message(message.chat.id,'Сгенерируем еще одну запись...', reply_markup = types.ReplyKeyboardRemove(selective=False))
			generate_req(bot, command, message)
		
		else:
			msg = bot.send_message(message.chat.id,'Выход...', reply_markup = types.ReplyKeyboardRemove(selective=False))
			del_mess(msg, bot, num+1)
			return

	password = pass_gen(command)
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	markup.add('Да')
	markup.add('Создать новую')
	markup.add('Выйти')

	mes = bot.send_message(message.chat.id,'Запись сгенерированна:\n\n'+password+'\n\nСохранить?', reply_markup = markup)
	bot.register_next_step_handler(mes, finish_gen)

def gen_pass_query(password, user_id):
	val_old = '/'
	part = name.split('/')

	if not os.path.isdir(way + '/' + '/'.join(part[:-1])):
		os.makedirs(way + '/'+'/'.join(part[:-1]))
	
	gpg = gnupg.GPG()
	gpg.encrypt(
        password,
        recipients=['user_'+user_id],
        output=way + '/' + name + '.gpg',
    )
