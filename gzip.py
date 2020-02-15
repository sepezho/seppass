import gzip

# from gzip import GzipFile
# from StringIO import StringIO
# from io import StringIO
# with open("Users_folder/user_707939820/gpg.gpg") as file_obj:
#     gz_data = file_obj.read().rstrip('\n')
# unescaped_data = gz_data.decode('string_escape')
# decompressed_data = gzip.GzipFile(fileobj=StringIO(unescaped_data)).read()
# print (decompressed_data)

# for data in gzip.GzipFile("Users_folder/user_707939820/gpg.gpg"):
#     print (data)


# import gzip
# # import StringIO

# compressed_data = """…Œþ|ÉqC3Äü
# êßˆÜÙß³(^Ã«E²©„Œ7³¦TíþF¶?æ+Íùêˆ"ñöªzè@¯p‡áê“d TÑ@CÇŠêhðQv«!WçÛÜæFV<FÓ%ï—´kl€Š]úÉ„Ö…–ùiÄè]ì¡E‚ÌVÿ¬ª#÷þl]/FDÝ»ÁuÉM„@¸´ì&ûIËA¦Á™»ñì†ÊC¼ÆÄ
# #'\ò€r˜ó€{ûVÃ°M(¡§¦p¬Q ëœ)+óxØ
# T^‹öŠÕBfD#DUz©¹ãêÅÄØ2­–ïžY{]ÜiÄowÒ¥ß9ÄÆ*j´¶	Žž«æÐòã½ÙXbÜÞ¾÷hÖ¥Bñå%ÁÈ,;ö
# H›ZKª7bFv
# Ã--CQjÄáWŸDµ{ ºë‰£ë8®¡:0i07°=³/ì­G4lu‰pMiÕ°ƒhÚœB«zï)@	\¼š\<ß±ñ/møkØ–Vã«³\q›Êüì†²?|Þy‹Ò>Í’2r1åOŒ÷<NÄ‹Ä…îé\Ñù%ý1ç Ýõ4Ø¯uªæéRo¯Ýwå•ãøv[6m¼P¢"""

# compressed_data = StringIO(compressed_data)
# print (compressed_data)

# for data in gzip.GzipFile(fileobj=compressed_data):
#     print (data)



import gzip
with gzip.open("Users_folder/user_707939820/gpg.gpg", 'rb') as f:
    file_content = f.read()
print(file_content)