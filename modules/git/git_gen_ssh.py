from Crypto.PublicKey import RSA
from os import system
from os import chmod
from os import path
from telebot import types

from del_mess import del_mess


def git_gen_ssh_main(message, bot):
	path_to_user_data = '/Seppass/Users_folder/user_'+str(message.chat.id)+'/user_data'
	
	if path.isfile(path_to_user_data+'/ssh_key.pub'):
		markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
		markup.add('Просмотреть существующий')
		markup.add('Создать новый')
		msg_handler = bot.send_message(message.chat.id, 'Я нашел ssh ключ. Ты хочешь создать новый или увидеть существующий?',reply_markup = markup)
		bot.register_next_step_handler(msg_handler, lambda msg: git_gen_request(msg, bot, path_to_user_data))
	
	else:
		git_gen_body(message, bot, path_to_user_data)


def git_gen_request(message, bot, path_to_user_data):
	
	if message.text == 'Просмотреть существующий':
		with open(path_to_user_data+'/ssh_key.pub', 'r') as key_pub:
			markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
			markup.add('Да')
			msg_handler = bot.send_message(message.chat.id, 'Вот ваш публичный ключ. Сами знаете куда его сувать...\n\n'+key_pub.read() + '\n\nЗакончили?',reply_markup = markup)
			bot.register_next_step_handler(msg_handler, lambda msg: end_get_git(msg, bot))
			return

	elif message.text == 'Создать новый':
		git_gen_body(message, bot, path_to_user_data)
	
	else:
		msg = bot.send_message(message.chat.id, 'Я тебя не понял ._.', reply_markup = types.ReplyKeyboardRemove(selective=False))
		del_mess(msg, bot, 4)
		return


def git_gen_body(message, bot, path_to_user_data):
	
	try:
		key = RSA.generate(4096)
		key_pub = None

		with open(path_to_user_data+'/ssh_key', 'wb') as content_file:
			content_file.write(key.exportKey('PEM'))
			chmod(path_to_user_data+'/ssh_key', int('0600', base=8))

		with open(path_to_user_data+'/ssh_key.pub', 'wb') as content_file:
			pubkey = key.publickey()
			key_pub = pubkey.exportKey('OpenSSH')
			content_file.write(pubkey.exportKey('OpenSSH'))
		
		ssh_code = '#!/bin/sh\nID_RSA='+path_to_user_data+'/ssh_key\nexec /usr/bin/ssh -o StrictHostKeyChecking=no -i $ID_RSA "$@"'
		
		with open(path_to_user_data+'/ssh_script.sh', 'w') as content_file:
			content_file.write(str(ssh_code))
			chmod(path_to_user_data+'/ssh_script.sh', int('0600', base=8))
		
		system('ssh-add ../Users_folder/user_'+str(message.chat.id)+'/user_data/token.txt')
		markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
		markup.add('Да')
		msg_handler = bot.send_message(message.chat.id, 'Вот ваш публичный ключ. Сами знаете куда его сувать...\n\n'+key_pub.decode("utf-8") + '\n\nЗакончили?',reply_markup = markup)
		bot.register_next_step_handler(msg_handler, lambda msg: end_get_git(msg, bot))
		return

	except:
		msg = bot.send_message(message.chat.id, 'Произошла ошибка.', reply_markup = types.ReplyKeyboardRemove(selective=False))
		del_mess(msg, bot, 2)
		return


def end_get_git(message, bot):
	msg = bot.send_message(message.chat.id, 'Теперь вы можете использовать git-комманды.', reply_markup = types.ReplyKeyboardRemove(selective=False))
	del_mess(msg, bot, 6)
	return