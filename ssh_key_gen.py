# from os import chmod
# from Crypto.PublicKey import RSA


from subprocess import Popen, PIPE
import shlex

def get_pub_key(path):
    args = shlex.split('ssh-keygen -y -f /Documents/seppass/new.key')
    # args.append(path)
    p = Popen(args, stdout=PIPE)
    stdout = p.communicate()[0]
    # if p.returncode != 0:
        # raise Exception("Error handling would be nice, eh?")
    print (str(stdout.strip()))
    return stdout.strip()

print (get_pub_key('/Documents/seppass/new.key'))










# key = RSA.generate(2048)
# with open("./ssh_keys/private.key", 'wb') as content_file:
#     chmod("./ssh_keys/private.key", int('0600'))
#     content_file.write(key.exportKey('PEM'))
    
#     print('priv -  '+ str(key.exportKey('PEM')))
# pubkey = key.publickey()
# with open("./ssh_keys/public.key", 'wb') as content_file:
    
#     content_file.write(pubkey.exportKey('OpenSSH'))
#     print('pub   -  ' + str(pubkey.exportKey('OpenSSH')))

# import base64

# import os
# from Crypto.PublicKey import RSA

# key = RSA.generate(2048, os.urandom)

# # Create public key.                                                                                                                                               
# ssh_rsa = '00000007' + base64.b16encode('ssh-rsa')

# # Exponent.                                                                                                                                                        
# exponent = '%x' % (key.e, )
# if len(exponent) % 2:
#     exponent = '0' + exponent

# ssh_rsa += '%08x' % (len(exponent) / 2, )
# ssh_rsa += exponent

# modulus = '%x' % (key.n, )
# if len(modulus) % 2:
#     modulus = '0' + modulus

# if modulus[0] in '89abcdef':
#     modulus = '00' + modulus

# ssh_rsa += '%08x' % (len(modulus) / 2, )
# ssh_rsa += modulus

# public_key = 'ssh-rsa %s' % (
#     base64.b64encode(base64.b16decode(ssh_rsa.upper())), )

# print(str(public_key))

# import os
# from base64 import b64encode
# from M2Crypto import RSA            

# key = RSA.gen_key(1024, 65537)
# raw_key = key.pub()[1]
# b64key = b64encode(raw_key)

# username = os.getlogin()
# hostname = os.uname()[1]
# keystring = 'ssh-rsa %s %s@%s' % (b64key, username, hostname)
# print(str(keystring))
# with open(os.getenv('HOME')+'/.ssh/id_rsa.pub') as keyfile:
    # keyfile.write(keystring)