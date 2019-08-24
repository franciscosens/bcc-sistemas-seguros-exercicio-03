import os

print('Digite o nome da pasta para ser criada: ', end='')
nome = input()

os.system('mkdir ' + nome)

