import os
import gnupg
import sqlite3
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
	
	# gpg = gnupg.GPG(gnupghome='/home/sepezho/.gnupg/')
	# encrypted_data = gpg.encrypt(message.text, str(message.from_user.id))
	
	gpg = gnupg.GPG()
	gpg.encrypt(
        message.text,
        # recipients=['user_'+str(message.from_user.id)],
        recipients='sepezho',
        output=way + '/' + name + '.gpg',
    )
	
	bot.send_message(message.chat.id,'Запись ' + name + ' добавлена.')



# print('======')

# gpg = gnupg.GPG(gnupghome='/home/sepezho/.gnupg/')
# try:
# 	keys = gpg.list_keys()
# 	key = gpg.search_keys('sepezho')
# 	print(keys)
# 	print('======')
# 	print(key)
# except TypeError as e:
# 	logger.error(msg='GNUPG TypeError: ' + str(e))

# print('======')

# def pgp_encrypt_file(data):
# 	gpg = gnupg.GPG(gnupghome='/home/sepezho/.gnupg/')

# 	conn = sqlite3.connect('DataBase.db', check_same_thread=False)
# 	c = conn.cursor()
# 	# query = "SELECT Key FROM Users WHERE User_id = '"+str(message.from_user.id)+"'"
# 	query = "SELECT Key FROM Users WHERE User_id = '"+str(707939820)+"'"
# 	key_fingerprint = c.execute(query).fetchall()[0][0]
# 	key_src = '/home/sepezho/.gnupg/openpgp-revocs.d/' + key_fingerprint + '.rev'

# 	try:
# 		with open(key_src) as file:
# 			key_data = file.read()
# 		print(key_data)
# 		print('=======')
# 		import_result = gpg.import_keys(key_data)
# 		print('Public key imported: {}'.format(key_fingerprint))
# 		public_keys = gpg.list_keys()
# 		fingerprint = public_keys[0]['fingerprint']

# 		# print('Attempting to encrypt file: ' + 'output_full_filepath')
# 		# with open(filepath, 'r') as f:
# 		# 	newfile = f.read()
# 		# newfile = 'output_full_filepath'
# 		status = gpg.decrypt(str(data), passphrase='EykNOfw5rkC{')

# 		print('status.ok : ' + str(status.ok))
# 		print('status.status : ' + str(status.status))
# 		print('asdads : ' + str(status))

# 	except FileNotFoundError as e:
# 		logger.error(msg='File not found: ' + str(e))
# 	except TypeError as e:
# 		print('GNUPG TypeError: ' + str(e))


# pgp_encrypt_file(dataa)