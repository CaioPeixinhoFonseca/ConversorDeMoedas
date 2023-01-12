import random
from time import sleep

sleep(1)
print('\033[32m   gerador de senha   \033[m')
caracteres = 'abcdefghijklmnopqrstuvwxyz1!2@3#$4567890%¨&*()`´-_=+°/?[{ª]};:.>,<|ABCDEFGHIJKLMNOPQRSTUVWXYZ'


numero = int(input('numero de senhas pra gerar: '))
numero = int(numero)

tamanho = int(input('tamanho da senha: '))
tamanho= int(tamanho)

sleep(1)
print('\nsenhas: ')

for pwd in range(numero):
    senhas = ''
    for c in range(tamanho):
        senhas += random.choice(caracteres)
    print(senhas)
    