import os
import sqlite3
import gnupg

# gpg = gnupg.GPG(gnupghome='/home/sepezho/.gnupg/')

# file_name = 'keyA'
# passphrase = 'myasdasdsae'
# name_real='seasdpezho'
# input_data = gpg.gen_key_input(
#     passphrase=passphrase,
# 	name_real= name_real)
# key = gpg.gen_key(input_data)
# key = key.fingerprint

# print('KEY CREATED: '+key)

# unencrypted_string = 'Who are you? How did you get in my house?'
# encrypted_data = gpg.encrypt(unencrypted_string, name_real)
# encrypted_string = str(encrypted_data)
# decrypted_data = gpg.decrypt(encrypted_string, passphrase=passphrase)

# print ('unencrypted_string: '+ unencrypted_string)
# print ('encrypted_string: '+ encrypted_string)
# print ('decrypted_data: '+ str(decrypted_data))


# -----------------------------
# ascii_armored_public_keys = gpg.export_keys(key, False)
# ascii_armored_private_keys = gpg.export_keys(key, True, passphrase=passphrase)
# with open(file_name+'.asc', 'w') as f:
#     f.write(ascii_armored_public_keys)
#     f.write(ascii_armored_private_keys)

# # print('KEY EXPORTED!')
# key = ''
# gpg.delete_keys(key, True, passphrase=passphrase)
# gpg.delete_keys(key)

# print('KEY DELETED!')

# key_data = open(file_name+'.asc').read()
# gpg.import_keys(key_data)

# print('KEY IMPORTED!')
# ---------------------------

# conn = sqlite3.connect('DataBase.db', check_same_thread=False)
# c = conn.cursor()
# query = "SELECT COUNT(*) FROM Users WHERE Username = 'sepezho'"
# c.execute(query)
# answer = c.fetchone()
# conn.commit()
# conn.close()

# print(answer)