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
# --------------main
