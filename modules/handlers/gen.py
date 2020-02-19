import os
import gnupg
import random
from telebot import types

def gen_main(message, bot):
	command = message.text.split()
	global way
	way = '/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id)
	if (len(command) == 4) and (command[1].find('//') == -1) and (command[1].find('.') == -1) and (command[1][-1] != '/'):
		global name
		name = command[1]
		if os.path.isfile(way +'/'+ name+'.gpg'):
			bot.send_message(message.chat.id, 'Такая запись уже существует.')
		else:
			part = name.split('/')
			if len(part) < 9:
				generate_req(bot, command, message)
			else:
				bot.send_message(message.chat.id,'Вы хотите создать очень много папок. Макс. глубина - 7 папок. Зачем вам столько -.-')
	else:
		bot.send_message(message.chat.id,'Используйте правильный синтаксис: /gen папка/имя_записи 12 1')
	
def pass_gen(command):
	password = ''
	if int(command[3]) == 0:
		chars = 'abn789opuv345qrst6fgcdelwxyz12hijk0'
	elif int(command[3]) == 1:
		chars = 'aghijEFGHIJzABCDKLMNklnop0qrstSTUVWXYZ123uvwxyOPQR456bcdef789'
	elif int(command[3]) == 2:
		chars = '+=_-)(*?:%;"!,}{[]><.~`/|abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
	else:
		bot.send_message(message.chat.id,'Сложность пароля варьируется от 0 до 2.')
		return

	for i in range(int(command[2])):
		password += random.choice(chars)
	return password

def generate_req(bot, command, message):

	def finish_gen(message):
		if message.text == 'Да':
			bot.send_message(message.chat.id,'Запись '+name+' сохранена.', reply_markup = types.ReplyKeyboardRemove(selective=False))
			gen_pass_query(password, str(message.from_user.id))
		elif message.text == 'Создать новую':
			bot.send_message(message.chat.id,'Сгенерируем еще одну запись...', reply_markup = types.ReplyKeyboardRemove(selective=False))
			generate_req(bot, command, message)
		else:
			bot.send_message(message.chat.id,'Выход...', reply_markup = types.ReplyKeyboardRemove(selective=False))
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
        # recipients=['user_'+user_id],
        recipients='sepezho',
        output=way + '/' + name + '.gpg',
    )
