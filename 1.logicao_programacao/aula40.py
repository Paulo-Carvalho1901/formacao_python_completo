"""Calculadora while"""

while True:

    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    # CRIADO UMA BANDEIRA
    numeros_validos = None

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



    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break