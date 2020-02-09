# -----------------------------------------------LSLSLSSLSLSLSLSLSL

   # ├── server
   # │   ├── git.gpg
   # │   ├── gitea.gpg
   # │   ├── sockduser.gpg
   # │   ├── admin.gpg
   # │   ├── root.gpg
   # │   └── zdvzds
   # │       ├── s.gpg
   # │       └── fold
   # │           └── asd.gpg
   # ├── games
   # │   ├── battleNet.gpg
   # │   ├── playStationNetwork.gpg
   # │   └── steam.gpg
   # ├── gitHub
   # │   ├── codes.gpg
   # │   └── gitHubPass.gpg
   # ├── mails
   # │   ├── PassAppServSepez.gpg
   # │   ├── sepezho.gpg
   # │   └── koko2kocit.gpg
   # ├── socialMedias
   # │   ├── vk.gpg
   # │   ├── stackOverflow.gpg
   # │   └── sounCloud.gpg
   # └── other
   #     ├── aliexpress.gpg
   #     ├── trello.gpg
   #     ├── Habr.gpg
   #     ├── codewars.gpg
   #     ├── freelanceH.gpg
   #     └── hh.gpg



			# pre_create_json(os.path.join(root, name))

		# roots = []
		# roots.append(root_folder)
			# -----------
			# rootsA = json.loads(roots)
			# data_for_folder = os.listdir(os.path.join(root, name))
			# rootsA[root+'/'+name] = []
			# for data in data_for_folder:
			# 	if not data.endswith('gpg'):

			# 		rootsA[root+'/'+name].append(root+'/'+name+'/'+data)
			# 	else:
			# 		rootsA[root+'/'+name].append(data)

			# roots = json.dumps(rootsA)
			# ------------
			# root_for_name = '/'.join(os.path.join(root, name).split('/')[:-1])
			# print(root_for_name)				
			# print(roots)				
			# roots.index(root_for_name)
			# is_exist = False

			# for n in roots:
			# 	if n == root_for_name:
			# 		is_exist = True

			# if is_exist:
			# 	print('exist')
			# else:
			# 	print('dont exist')
			# 	roots.append(root_for_name)

# def pre_create_json(src):
# 	global roots
# 	rootsA = json.loads(roots)
# 	rootsA[src] = []
# 	rootsb = create_json(src, rootsA)
# 	roots = json.dumps(rootsb)

# def create_json(src, rootsA):
# 	# global roots
# 	print('1\n')
# 	# rootsA = json.loads(roots)
# 	data_for_folder = os.listdir(src)
# 	for data in data_for_folder:
# 		if not data.endswith('gpg'):
# 			sd = src+'/'+data
# 			rootsA[src].append(sd)
# 			z = create_json(os.path.join(src, data), rootsA)
# 			rootsA[src][sd].append(z)
# 		else:
# 			print(data)
# 			rootsA[src].append(data)
# 	return rootsA
	# roots = json.dumps(rootsA)

			# dirsA.append(os.path.join(root, name))
		# for file in files:
		# 	if file.endswith(".gpg"):
		# 		dirsA.append(os.path.join(root, file))


# _______________________________
	# # dirsA.append('Users_folder/user_'+str(message.from_user.id))
	# dirs = sorted(dirsA)
	# print(dirs)
	# # i = 0
	# arr = []
	# name_old = dirs[0]
	# z = True
	# old_path = ''
	# for name in dirs:
	# 	for path in name:
	# 		if not path.endswith(".gpg"):
	# 			if old_path = path:
	# 				# name_arr = name.split('/')[2:]
	# 				resp += '----------------\n' + path + '\n'
	# 			else:

	# 	# name_old = name
	# 	# name_arr = name.split('/')[2:]
	# 	# name_old_arr = name_old.split('/')[2:]
	# 	# arr.append(name_arr)
	# 	# print(name)
	# 	index = dirs.index(name)
	# 	while z:
	# 		name_arr = dirs[index+1].split('/')[2:]
	# 		name_old_arr = dirs[index].split('/')[2:]
	# 		print(name_arr)
	# 		print(name_old_arr)
	# 		index += 1
	# 		if name_arr[0] == name_old_arr[0]:
	# 			resp += '----------------\n' + str(name_arr[0]) + '\n'
	# 		else:
	# 			z = False
	# 		# resp += str(name_arr[-1]) + '\n'
	# 		resp += str(name_old_arr[-1]) + '\n'
	# 	# for folder in name_arr[:-1]
# _______________________________

	# 	line = ''
	# 	i = i+1
	# 	if len(os.listdir(name)) == i:
	# 		resp = resp + line + '└──' + name.split('/')[-1] +'\n'
	# 		line = line + '    '
	# 	else:
	# 		resp = resp + line +'├──' + name.split('/')[-1] +'\n'
	# 		line = line + '|  '
	# 	j = 0
	# 	for file in os.listdir(name):
	# 		j = j+1
	# 		if len(os.listdir(name)) == j:
	# 			if file.endswith(".gpg"):
	# 				resp = resp + line + '   └──' + file +'\n'
	# 		else:
	# 			if file.endswith(".gpg"):
	# 				resp = resp + line + '   ├──' + file +'\n'



# ----------------

# def line(root, name, root_folder):
# 	way = os.path.join(root, name).split('/')
# 	way = way[2:][::-1]
# 	line = ''
# 	i=0
# 	for folder in way:
# 		i = i+1
# 		depth_path = os.path.join(root_folder, '/'.join(way[::-1][:-i]))
# 		listdir = os.listdir(depth_path)
# 		num = listdir.index(folder)
# 		if len(os.listdir(depth_path)) == num:
# 			line = line + '   '
# 		else:
# 			line = line + '|  '
# 	return line

			# # line = ''
			# i = i+1
			# if len(dirs) == i:
			# 	resp = resp + line(root, name, root_folder) + '└──' + os.path.join(name) +'\n'
			# 	# line = line + '    '
			# else:
			# 	resp = resp + line(root, name, root_folder) +'├──' + os.path.join(name) +'\n'
			# 	# line = line + '|  '
			# j = 0
			# for file in os.listdir(os.path.join(root, name)):where
			# 	j = j+1
			
			# 	if len(os.listdir(os.path.join(root, name))) == j:
			# 		if file.endswith(".gpg"):
			# 			resp = resp + line(root, name, root_folder) + '   └──' + file +'\n'
			# 	else:
			# 		if file.endswith(".gpg"):
			# 			resp = resp + line(root, name, root_folder) + '   ├──' + file +'\n'
# ----------------
			# line = ''
			# i = i+1
			# if len(dirs) == i:
			# 	resp = resp + line + '└──' + os.path.join(name) +'\n'
			# 	line = line + '    '
			# else:
			# 	resp = resp + line +'├──' + os.path.join(name) +'\n'
			# 	line = line + '|  '
			# j = 0
			# for file in os.listdir(os.path.join(root, name)):
			# 	j = j+1
			
			# 	if len(os.listdir(os.path.join(root, name))) == j:
			# 		if file.endswith(".gpg"):
			# 			resp = resp + line + '   └──' + file +'\n'
			# 	else:
			# 		if file.endswith(".gpg"):
			# 			resp = resp + line + '   ├──' + file +'\n'


# ----------------
	# src = 'Users_folder/user_'+str(message.from_user.id)

	# line = '├──'
	# resp = object()
	# fun('Users_folder/user_'+str(message.from_user.id), message, resp)
	# print(resp)

	# for dir_name, dirs, files in os.walk('Users_folder/user_'+str(message.from_user.id)):
	# 	print(dir_name, len(dirs))

# user_707939820
# ├──1
# ├──2
# │    |──asdasd.gpg
# │    ├──2.1
# │    └──2.2
# │            └──opasihdfpaoshf.gpg
# └──3
#        └──3.1
# def fun(path, message, resp):
# 	for thing in os.listdir(path):
# 		resp.thing
# 		print(resp)
# 		for n in resp:
# 			if not (n.endswith(".gpg") or n.endswith(".txt")) :
# 				fun(path + '/' + n, message, resp)

	# for dir_name, dirs, files in os.walk(src):
	# 	print(dir_name, len(dirs))

			# -------------------
# 	fun('Users_folder/user_'+str(message.from_user.id), message, resp)



# def fun(path, message, resp):
# 	i = 0
# 	for thing in os.listdir(path):
# 		line = '│    '*(len(path.split('/'))-3)
# 		# line = '│    '
# 		i = i+1
# 		j = 0
# 		stick = '|'
# 		if thing.endswith(".gpg") or thing.endswith(".txt") :
# 			if not thing.endswith(".txt"):
# 				j = j+1
# 				if len(thing) == j-1:
# 					resp = resp + line + stick + '    └──' + thing +'\n'
# 				else:
# 					resp = resp + line + stick + '    ├──' + thing +'\n'
# 				bot.send_message(message.chat.id, resp)
# 				print(resp)
# 				fun(path + '/' + thing, message, resp)

# 		else:
# 			if len(thing) == i:
# 				resp = resp + line + '└──' + thing +'\n'
# 				stick = ''
# 			else:
# 				resp = resp + line + '├──' + thing +'\n'
# 				stick = '│'
# 			fun(path + '/' + thing, message, resp)



			# for file in os.listdir('Users_folder/user_'+str(message.from_user.id) +'/'+ thing):
				# if len(thing) == j:
						# resp = resp + line + stick + '    └──' + file +'\n'
				# else:
						# resp = resp + line + stick + '    ├──' + file +'\n'
				# j = j+1

			# -------------------

	# for root, dirs, files in os.walk('Users_folder/user_'+str(message.from_user.id), topdown=True):
	# 	i = 0
	# 	for name in dirs:
	# 		line = '│    '*(len(os.path.join(root, name).split('/'))-3)
	# 		i = i+1
	# 		if len(dirs) == i:
	# 			resp = resp + line + '└──' + os.path.join(name) +'\n'
	# 			stick = ''
	# 		else:
	# 			resp = resp + line + '├──' + os.path.join(name) +'\n'
	# 			stick = '│'

	# 		j = 0
	# 		for file in os.listdir(os.path.join(root, name)):
	# 			if len(dirs) == j:
	# 				if file.endswith(".gpg"):
	# 					resp = resp + line + stick + '    └──' + file +'\n'
	# 			else:
	# 				if file.endswith(".gpg"):
	# 					resp = resp + line + stick + '    ├──' + file +'\n'
	# 			j = j+1

		# for name in files:
		# 	print(root[13:])
		# 	print(name)

		# 	if root[13:] == ('user_' + str(message.from_user.id)):
		# 		print(os.path.join(name))
		# 	else:
		# 		print(os.path.join(root[13:], name))
		# for name in files:
		# 	print(os.path.join(root, name))

			# print('+++++++++++++\n')
			# print(os.path.join(root, name)+'\n')
			# print(os.listdir(os.path.join(root, name)))
				# print(os.listdir(o.path.join(root, name)))
			# for root, dirs, files in os.walk(os.path.join(root, name), topdown=True):
				# for namea in files:
					# print('----------------\n')
					# print(namea+'\n')
					# resp = resp + '----------------\n'+ os.path.join(root, namea) +'\n'

# -----------------------------------------------LSLSLSSLSLSLSLSLSL




# ---------------auth
# def sign_begin(message):
# 	msg = bot.send_message(message.chat.id, 'Введите пароль.')
# 	bot.register_next_step_handler(msg, sign_response)

# def sign_response(message):
# 	with open('/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) + '/Nothing.txt', 'r') as f:
# 		password = f.read()
# 	if password == message.text:
# 		main(message, bot)
# 	else:
# 		msg = bot.send_message(message.chat.id, 'Вы ввели пароль не верно. Повторите ввод.')
# 		bot.register_next_step_handler(msg, login_response)

# def start_response(message):
# 	if message.text == 'Вход':
# 		sign_begin(message)
# 	elif message.text == 'Регистрация':
# 		login_begin(message)
# 	else:
# 		bot.send_message(message.chat.id, 'Непонел.', reply_markup = types.ReplyKeyboardRemove(selective=False))

# def login_begin(message):
# 	conn = sqlite3.connect('DataBase.db', check_same_thread=False)
# 	c = conn.cursor()
# 	query = "SELECT COUNT(*) FROM Users WHERE User_id = '"+str(message.from_user.id)+"'"
# 	c.execute(query)
# 	answer = c.fetchone()
# 	conn.commit()
# 	conn.close()

# 	if answer == (0,):
# 		settings_pre_begin(message, bot)
# 	else:
# 		bot.send_message(message.chat.id, 'Ваш телеграм уже связан с вашим акк для этого бота.\n\nВойдите в акк, отправив снова /start', reply_markup = types.ReplyKeyboardRemove(selective=False))
# ---------------auth



# --------------main
# query = "SELECT Settings FROM Users WHERE User_id = '"+str(message.from_user.id)+"'"
# res = c.execute(query).fetchall()[0][0]
# res = res.replace("'", '"')
# res_parse = json.loads(res)
# print(res)
# if res_parse["store_pass"] == 'pass_on_serv':
# 	main(message, bot)
# else:
# 	sign_begin(message)

# def sign_begin(message):
# 	msg = bot.send_message(message.chat.id, 'Введите пароль.')
# 	bot.register_next_step_handler(msg, sign_response)

# def sign_response(message):
# 	with open('/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) + '/Nothing.txt', 'r') as f:
# 		password = f.read()
# 	if password == message.text:
# 		main(message, bot)
# 	else:
# 		msg = bot.send_message(message.chat.id, 'Вы ввели пароль не верно. Повторите ввод.')
# 		bot.register_next_step_handler(msg, login_response)

	gpg = gnupg.GPG(gnupghome='/home/sepezho/.gnupg/')

	unencrypted_string = 'Aasdasd'
	signed_data = gpg.sign(unencrypted_string, keyid = 'AB37921A79EB5272EB6DE199BE7A9DF6AF303FF0', passphrase=str(message.text), extra_args=['--passphrase-fd'])
	# encrypted_data = gpg.encrypt(unencrypted_string, str(message.from_user.id), True)
	 # clearsign=False, detach=True, binary=True
	# print ('unencrypted_string: '+ unencrypted_string)
	# encrypted_string = str(encrypted_data)
	# print ('encrypted_string: '+ encrypted_string)
	# decrypted_data = gpg.decrypt(encrypted_string, passphrase=message.text)
	# print ('decrypted_data: '+ str(decrypted_data))

	print(str(signed_data))


	# unencrypted_string = 'Who are you? How did you get in my house?'
	# encrypted_data = gpg.encrypt(unencrypted_string, str(message.from_user.id))
	# encrypted_string = str(encrypted_data)
	# decrypted_data = gpg.decrypt(encrypted_string, passphrase=str(message.text), extra_args=[])

	# print ('ok: ' + str(decrypted_data.ok))
	# print ('status: '+ decrypted_data.status)
	# print ('stderr: '+ decrypted_data.stderr)
	# print ('decrypted string: '+ str(decrypted_data.data))


	# if unencrypted_string == str(decrypted_data):
		# bot.send_message(message.chat.id, 'Чикибамбони')
	# else:
		# bot.send_message(message.chat.id, 'Ошибка')

	# @bot.message_handler(commands=['insert'])
	# def insert_func_in_main(message):
	# 	insert_main(message, bot)


# --------------main


