import random

print(" Seja bem vindo ao gerador de senha!!")

caract = 'abcdefghijklmnopqrstwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*()'

numeros = int(input('Número de senhas para serem geradas: '))

tamanho = int(input('Insira o tamanho da senha desejada: '))

print('\n As senhas geradas é são: ')
   #loop for
for senha in range(numeros):
    senhas = ''
    for c in range(tamanho):
        senhas += random.choice(caract)
    print(senhas)


input()



