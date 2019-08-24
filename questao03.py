import re
import os

print('Digite o nome da pasta para ser criada: ', end='')
nome = input()

os.mkdir(nome)