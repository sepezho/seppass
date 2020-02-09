import os
import json 

def ls_main(message, bot):
	# resp = 'user_'+str(message.from_user.id) + '\n'
	true_root = 'Users_folder/user_'+str(message.from_user.id)
	resp = []
	for root, dirs, files in os.walk(true_root):
		for name in dirs:
			resp.append(root+ '/' +name)
			for file in sorted(os.listdir(os.path.join(root, name))):
				if file.endswith(".gpg"):
					resp.append(root+ '/' +name + '/' +file)
	# print(resp)
	resp = sorted(resp)
	for data in resp:
		# if not data.endswith('.gpg'):
		# print(data)
		ls = sorted(os.listdir('/'.join(data.split('/')[:-1])))
		index = ls.index(''.join(data.split('/')[-1]))
		# print(ls)
		# print(index)
		if len(ls) == index + 1:
			index_data = resp.index(data)
			resp[index_data] =  line(data , true_root)+'└── '+''.join(data.split('/')[-1]) 
		else:
			index_data = resp.index(data)
			resp[index_data] =  line(data, true_root)+'├── '+''.join(data.split('/')[-1]) 
	response = ''
	for data in resp:
		response += data[4:]+'\n'
	print('------------------------\n'+str(response)+'\n------------------------\n')
	bot.send_message(message.chat.id, response)


def line(src, true_root):
	way = src.split('/')
	way = way[2:][::-1]
	print(way)
	line = ''
	i=0
	for folder in way:
		i = i+1
		depth_path = os.path.join(true_root, '/'.join(way[::-1][:-i]))
		print(depth_path)
		listdir = sorted(os.listdir(depth_path))
		num = listdir.index(folder)
		if len(listdir) == num+1:
			line = line+'    '
		else:
			line = line+'│   '
	print(line+'\n------------')
	return line


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
		# roots.append(true_root)
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

# def line(root, name, true_root):
# 	way = os.path.join(root, name).split('/')
# 	way = way[2:][::-1]
# 	line = ''
# 	i=0
# 	for folder in way:
# 		i = i+1
# 		depth_path = os.path.join(true_root, '/'.join(way[::-1][:-i]))
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
			# 	resp = resp + line(root, name, true_root) + '└──' + os.path.join(name) +'\n'
			# 	# line = line + '    '
			# else:
			# 	resp = resp + line(root, name, true_root) +'├──' + os.path.join(name) +'\n'
			# 	# line = line + '|  '
			# j = 0
			# for file in os.listdir(os.path.join(root, name)):where
			# 	j = j+1
			
			# 	if len(os.listdir(os.path.join(root, name))) == j:
			# 		if file.endswith(".gpg"):
			# 			resp = resp + line(root, name, true_root) + '   └──' + file +'\n'
			# 	else:
			# 		if file.endswith(".gpg"):
			# 			resp = resp + line(root, name, true_root) + '   ├──' + file +'\n'
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