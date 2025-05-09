"""Calculadora while"""

while True:

    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    # CRIADO UMA BANDEIRA
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    # CRIADO VALIDAÇÃO DOS NUMEROS
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    # CRIADO VALIDAÇÃO NUMEROS VALIDOS
    if numeros_validos is None:
        print('Um ou ambos dos números digitados não são inválidos.')
        continue
    
    # CRIADO VALIDAÇÃO DOS OPERADORES SOLICITADOS
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    # CROADO VALIDAÇÃO PARA QUANTIDADE DE OPERADORES DIGITADAS
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    # CRIADO AS OPERAÇÕES MATEMATICAS
    print('Realizando sua conta, confira o resultado a abaixo')

    if operador == '+':
        print(f'{num_1_float}+{num_2_float}=', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float}-{num_2_float}=', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float}/{num_2_float}=', num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float}*{num_2_float}=', num_1_float * num_2_float)
    else:
        print('Não deve chegar até aqui.')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break