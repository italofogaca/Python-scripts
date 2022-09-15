## teste primeira calculadora

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print(' Escolha a operação desejada :) : ')
print('1- Soma (+)')
print('2- Subtração (-)')
print('3- Multiplicação (x)')
print('4- Divisão (/)')

choice = input('Digite a opção escolhida: ')

num1 = int(input('\n Digite o primeiro número: \n'))
num2 = int(input('\n Digite o segundo número: \n'))

if choice == '1':
    print("\n")
    print(num1, '+', num2, '=', add(num1, num2))
    print("\n")

elif choice == '2':
    print("\n")
    print(num1, '-', num2, '=', subtract(num1, num2))
    print("\n")

elif choice == '3':
    print("\n")
    print(num1, '*', num2, '=', multiply(num1, num2))
    print("\n")

elif choice == '4':

    print("\n")
    print(num1, '/', num2, '=', divide(num1, num2))
    print("\n")

else:
    print("\n")
    print('Opção inválida, por favor, digite novamente. ')
    print("\n")

input()

