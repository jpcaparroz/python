num1 = 2
num2 = 5.7
num3 = num1 + num2

print(type(num1), type(num2), type(num3))


# Potencia
print(num1 ** 5)

# Verificação de maior
print(5 > 2)

# Verificação com IF
idade = 15

if idade >= 18:
    
    print('Acesso liberado!')
    
else: print("NEGADO!")


## Módulo math
import math

# Raiz quadrada
print(math.sqrt(16))

# Fatorial
print(math.factorial(5))


## Inputando dados no terminal
num1 = int(input('Digite um número:'))
num2 = int(input('Digite outro número:'))

print('O resultado de', num1, '+', num2, ' e igual a:', num1 + num2)


## Exercicio média ponderada
peso_prova1 = int(input('Digite o peso da prova 1: '))
peso_prova2 = int(input('Digite o peso da prova 2: '))

nota1 = int(input('Digite a nota da 1º prova: '))
nota2 = int(input('Digite a nota da 2º prova: '))

media_ponderada = ((peso_prova1 * nota1 ) + (peso_prova2 * nota2)) / (peso_prova1 + peso_prova2)

print('A media ponderada e igual a: ', media_ponderada)