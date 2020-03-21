from os import makedirs
from os import path
from gnupg import GPG
from random import choice
from telebot import types
from del_mess import del_mess


def gen_main(message, bot):
	command = message.text.split()
	
	path_to_user_folder = '/home/sepezho/Documents/Seppass/Users_folder/user_' + str(message.from_user.id)+'/main'
	
	if (len(command) == 4) and (command[1].find('//') == -1) and (command[1].find('.') == -1) and (command[1][0] != '/') and (command[1][-1] != '/'):
		name = command[1]
		
		if not path.isfile(path_to_user_folder +'/'+ name+'.gpg'):
			if not path.isdir(path_to_user_folder +'/'+ name):
				if len(name.split('/')) < 9:
					if int(command[2]) < 26:
						generate_req(message, bot, command, path_to_user_folder, name)

					else:
						msg = bot.send_message(message.chat.id,'Макс. длина генерации - 25 симболов.')
						del_mess(msg, bot, 2)
						return

				else:
					msg = bot.send_message(message.chat.id,'Вы хотите создать очень много папок. Макс. глубина - 7 папок. Зачем вам столько -.-')
					del_mess(msg, bot, 2)
					return

			else:
				msg = bot.send_message(message.chat.id,'Папка с таким названием уже сужествует в этой директории.\n\n')
				del_mess(msg, bot, 2)
				return

		else:
			msg = bot.send_message(message.chat.id,'Файл с таким названием в этой папке уже существует.\n\n')
			del_mess(msg, bot, 2)
			return

	else:
		msg = bot.send_message(message.chat.id,'Используйте правильный синтаксис: /gen папка/имя_записи 12 1')
		del_mess(msg, bot, 2)
		return


def pass_gen(command):
	password = ''
	
	if int(command[3]) == 0:
		chars = 'abgoBCDPpqrstuAQRSEFGHIJvwxyZ123456zKWhijklnXY7890LMNcdefOTUV'
	
	elif int(command[3]) == 1:
		chars = '"c(lnop234qrBCDvwEFstuxyz+=*?:%;AGHdefgh-)IJKL<.~`/|M189N567ijk_OPQRSTUV!,}{[]>abWXYZ0'
	
	elif int(command[3]) == 2:
		chars = '+-)=_GHI<.~`/|abcde_-)=_GHIJKLMNOP{[]><.~ghrstu:%;"!,}9JKLMNOP{[]>vwxy=_zABC{[]>ijklnopq<.~`/|+XYZ1234%;"!,}56EFQRSTUVW(*?:78-)(*?0'
	
	else:
		msg = bot.send_message(message.chat.id,'Сложность пароля варьируется от 0 до 2.')
		del_mess(msg, bot, 2)
		return

	# USED SYMBOLS: "+=_-)(*?:%;"!,}{[]><.~`/|abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
	for i in range(int(command[2])):
		password += choice(chars)
	
	return password


num = 0
def generate_req(message, bot, command, path_to_user_folder, name):
	global num
	num += 3

	def finish_gen(message):
		if message.text == 'Да':
			try:
				gen_pass_query(password, str(message.from_user.id), path_to_user_folder, name)
				msg = bot.send_message(message.chat.id,'Запись '+name+' сохранена.', reply_markup = types.ReplyKeyboardRemove(selective=False))
				del_mess(msg, bot, num+1)
				return

			except TypeError as e:
				msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
				del_mess(msg, bot, num+1)
				return

		elif message.text == 'Сгенерировать новую':
			bot.send_message(message.chat.id,'Сгенерируем еще одну запись...', reply_markup = types.ReplyKeyboardRemove(selective=False))
			generate_req(message, bot, command, path_to_user_folder, name)
		
		else:
			msg = bot.send_message(message.chat.id,'Выход...', reply_markup = types.ReplyKeyboardRemove(selective=False))
			del_mess(msg, bot, num+1)
			return

	password = pass_gen(command)
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	markup.add('Да')
	markup.add('Сгенерировать новую')
	markup.add('Выйти')

	mes = bot.send_message(message.chat.id,'Запись сгенерированна:\n\n'+password+'\n\nСохранить?', reply_markup = markup)
	bot.register_next_step_handler(mes, finish_gen)


def gen_pass_query(password, user_id, path_to_user_folder, name):
	val_old = '/'
	part = name.split('/')

	if not path.isdir(path_to_user_folder + '/' + '/'.join(part[:-1])):
		makedirs(path_to_user_folder + '/'+'/'.join(part[:-1]))
	
	gpg = GPG()
	gpg.encrypt(
        password,
        recipients = ['user_'+user_id],
        output = path_to_user_folder + '/' + name + '.gpg',
    )
