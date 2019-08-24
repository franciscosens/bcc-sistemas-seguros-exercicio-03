import re
import os

print('Digite o nome da pasta para ser criada: ', end='')
nome = input()
resultado = re.fullmatch(r'([a-zA-Zà-úÀ-Ú0-9\s]*)', nome)

if resultado:
    print('Criando pasta')
    os.system('mkdir ' + nome)
else:
    print('SO Injection detectada')

