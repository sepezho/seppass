import os
import shutil
from telebot import types

def rm_main(message, bot):
	command = message.text.split()
	name = command[1]
	if len(command) == 2:
		if os.path.isfile('/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) +'/'+ name+'.gpg'):
			os.remove('/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) + '/' + name + '.gpg')
			bot.send_message(message.chat.id, 'Запись '+name+' удалена.')
		elif os.path.isdir('/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) +'/'+ name):
			markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
			markup.add('Да, я уверен', 'Нет')
			msg = bot.send_message(message.chat.id, 'Вы уверены, что хотите удалить папку '+name+' и все ее содержимое?'+ ls_folder(message, name), reply_markup = markup)
			def finish_rm_folder(message):
				if message.text == 'Да, я уверен':
					shutil.rmtree('/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) + '/' + name)
					bot.send_message(message.chat.id, 'Папка '+name+', и все ее содержимое удалено.', reply_markup = types.ReplyKeyboardRemove(selective=False))
				else:
					bot.send_message(message.chat.id, 'Отмена.', reply_markup = types.ReplyKeyboardRemove(selective=False))
			bot.register_next_step_handler(msg, finish_rm_folder)
		else:
			bot.send_message(message.chat.id, 'Такой записи не существует.')
	else:
		bot.send_message(message.chat.id,'Используйте правильный синтаксис: /rm папка/имя_записи')
		return

def ls_folder(message, name):
	root_folder = 'Users_folder/user_'+str(message.from_user.id)
	response_arr = []
	for root, dirs, files in os.walk(root_folder):
		for dir_ in dirs:
			if root+ '/' +dir_ == root_folder + '/' +name:
				response_arr.append(root+ '/' +dir_)
				for file in sorted(os.listdir(root+ '/' +dir_)):
					if file.endswith(".gpg"):
						response_arr.append(root+ '/' +dir_ + '/' +file)
	response_arr = sorted(response_arr)
	for file in response_arr:
		ls = sorted(os.listdir('/'.join(file.split('/')[:-1])))
		index = ls.index(''.join(file.split('/')[-1]))
		index_file = response_arr.index(file)
		last_symbol = '╠══ '
		if len(ls) == index + 1:
			last_symbol = '╚══ '
		file_name = ''.join(file.split('/')[-1])
		if file_name.endswith(".gpg"):
			response_arr[index_file] =  line(file, root_folder, name)+last_symbol+file_name[:-4]
		else:
			response_arr[index_file] =  line(file, root_folder, name)+last_symbol+'📂'+file_name

	response_text = '╠══════════════════════════════════╣\n\n'+'		📂'+name+'\n		╔══════════════\n'
	ij = False
	for response_arr_text in response_arr:
		# if ij:
		response_text +='		'+response_arr_text+'\n'
		ij = True
	response_text +='\n╠══════════════════════════════════╣'
	return response_text

def line(way, root_folder, name):
	way = way.split('/')
	deepth = len((root_folder+'/'+name).split('/'))
	way = way[deepth:][:-1][::-1]
	line = ''
	i=0
	for folder in way:
		i = i+1
		depth_path = root_folder+'/'+'/'.join(way[::-1][:-i])
		listdir = sorted(os.listdir(depth_path))
		num = listdir.index(folder)
		if len(listdir) == num+1:
			line = '       '+line
		else:
			line = '║      '+line
	return line
