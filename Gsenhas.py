import random

print('\033[47m \033[93m Ｇｅｒａｄｏｒ ｄｅ ｓｅｎｈａｓ\033[00m')

caracteres = 'abcdefghijklmnopqrstuvwlxyz123456789'
qtsenhas = int(input('𝘿𝙞𝙜𝙞𝙩𝙚 𝙖 𝙦𝙪𝙖𝙣𝙩𝙞𝙙𝙖𝙙𝙚 𝙙𝙚 𝙨𝙚𝙣𝙝𝙖𝙨 𝙦𝙪𝙚 𝙙𝙚𝙨𝙚𝙟𝙖 𝙜𝙚𝙧𝙖𝙧: '))
senha = int(input('𝙙𝙞𝙜𝙞𝙩𝙚 𝙖 𝙦𝙪𝙖𝙣𝙩𝙞𝙙𝙖𝙙𝙚 𝙙𝙚 𝙘𝙖𝙧𝙖𝙘𝙩𝙚𝙧𝙚𝙨 𝙦𝙪𝙚 𝙨𝙪𝙖 𝙨𝙚𝙣𝙝𝙖 𝙩𝙚𝙧: '))

print('\033[46m𝙢 𝙎𝙪𝙖𝙨 𝙨𝙚𝙣𝙝𝙖𝙨 𝙨𝙖𝙤: \033[00m')
for i in range(qtsenhas):
    senhasgeradas = ''
    for j in range(senha):
        senhasgeradas += random.choice(caracteres)
    print('\033[31m',senhasgeradas)


