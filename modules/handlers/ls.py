import os

def ls_main(message, bot):
	root_folder = 'Users_folder/user_'+str(message.from_user.id)
	response_arr = []
	for root, dirs, files in os.walk(root_folder):
		for dir_ in dirs:
			response_arr.append(root+ '/' +dir_)
			for file in sorted(os.listdir(os.path.join(root, dir_))):
				if file.endswith(".gpg"):
					response_arr.append(root+ '/' +dir_ + '/' +file)
	response_arr = sorted(response_arr)
	for file in response_arr:
		ls = sorted(os.listdir('/'.join(file.split('/')[:-1])))
		index = ls.index(''.join(file.split('/')[-1]))
		if len(ls) == index + 1:
			index_file = response_arr.index(file)
			response_arr[index_file] =  line(file , root_folder)+'└── '+''.join(file.split('/')[-1]) 
		else:
			index_file = response_arr.index(file)
			response_arr[index_file] =  line(file, root_folder)+'├── '+''.join(file.split('/')[-1]) 
	response_text = '---------------------------------------------------------------\n\n'+'user_'+str(message.from_user.id) + '\n'
	for response_arr_text in response_arr:
		response_text += response_arr_text+'\n'
	response_text += '\n---------------------------------------------------------------'
	bot.send_message(message.chat.id, response_text)

def line(way, root_folder):
	way = way.split('/')
	way = way[2:][:-1][::-1]
	line = ''
	i=0
	for folder in way:
		i = i+1
		depth_path = os.path.join(root_folder, '/'.join(way[::-1][:-i]))
		listdir = sorted(os.listdir(depth_path))
		num = listdir.index(folder)
		if len(listdir) == num+1:
			line = '    '+line
		else:
			line = '│   '+line
	return line
