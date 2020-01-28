import gnupg
from pprint import pprint
gpg = gnupg.GPG(gnupghome='/home/sepezho/.gnupg/')

# key = 'F308143BC139F61C06D060412C4577FE97C3E455'
# ascii_armored_public_keys = gpg.export_keys(key)
# ascii_armored_private_keys = gpg.export_keys(key, True)
# with open('mykeyfile.asc', 'w') as f:
#     f.write(ascii_armored_public_keys)
#     f.write(ascii_armored_private_keys)


# key_data = open('pubkey.asc').read()
# import_result = gpg.import_keys(key_data)
# pprint(import_result.results)

# unencrypted_string = 'Who are you? How did you get in my house?'
# encrypted_data = gpg.encrypt(unencrypted_string, 'sepezho@gmail.com')
# encrypted_string = str(encrypted_data)


unencrypted_string = 'Who are you? How did you get in my house?'
encrypted_data = gpg.encrypt(unencrypted_string, 'sepezho@gmail.com')
encrypted_string = str(encrypted_data)
decrypted_data = gpg.decrypt(encrypted_string, passphrase='EykNOfw5rkC{')

print ('status: '+ encrypted_data.status)
print ('stderr: '+ encrypted_data.stderr)
print ('unencrypted_string: '+ unencrypted_string)
print ('encrypted_string: '+ encrypted_string)
print ('decrypted_data: '+  str(decrypted_data))

