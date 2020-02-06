import os
def ls_main(message, bot_old):
	global bot
	bot = bot_old
	resp = 'user_'+str(message.from_user.id) + '\n'
	for root, dirs, files in os.walk('Users_folder/user_'+str(message.from_user.id), topdown=True):
		i = 0
		for name in dirs:
			line = '│    '*(len(os.path.join(root, name).split('/'))-3)
			i = i+1
			if len(dirs) == i:
				resp = resp + line + '└──' + os.path.join(name) +'\n'
				stick = ''
			else:
				resp = resp + line +'├──' + os.path.join(name) +'\n'
				stick = '│'
			j = 0
			for file in os.listdir(os.path.join(root, name)):
				j = j+1
				print(len(os.listdir(os.path.join(root, name))))
				if len(os.listdir(os.path.join(root, name))) == j:
					if file.endswith(".gpg"):
						resp = resp + line + stick + '    └──' + file +'\n'
				else:
					if file.endswith(".gpg"):
						resp = resp + line + stick + '    ├──' + file +'\n'
	print(resp)
	bot.send_message(message.chat.id, resp)




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