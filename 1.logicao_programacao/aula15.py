# coletando dados do usuário
# toda informação capiturada pelo inpu reotna uma string

nome = input('Qual é seu nome? ')
print(f'O seu nome é {nome=}')

# input sempre retorna uma string
numero = input('Digite números: ')
print(f'O números digitado foi {type(numero), numero}')

# Nessa parte do código os dois numero esta como str
numero_1 = input('Digite o número 1: ')
numero_2 = input('Digite o número 2: ')

# Está acontecendo a concatenação
# para resolver essa problema temos que fazer a coerçao de tipos ou "casting"
numero_1_int = int(numero_1)
numero_2_int = int(numero_2)

soma = numero_1_int + numero_2_int
print(f'A soma dos numeros são: {soma}')
