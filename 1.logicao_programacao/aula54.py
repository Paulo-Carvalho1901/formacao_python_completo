"""
Faça uma lista de compra com listas
o usuario deve ter a possibilidade de 
inserir, apagar, e listar valores de sua lista
Não permita que o programa quebre com 
error de índices inexistentes na lista
"""

import os

lista = []

while True:
    # criadno condição para interação com usuário
    print('Selecione uma opção:')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    # criando estrutura de controle para as opções
    if opcao == 'i':
        os.system('cls')
        valor = input('valor: ')
        lista.append(valor)
    elif opcao == 'a':
        print('a')
    elif opcao == 'l':
        # limpando o terminal
        os.system('cls')
        # verificando se alista está vazia
        if len(lista) == 0:
            print('Não há nada para lista')

        # Iterando na lista com o index usando unumerate
        # caso tenha algo na lista
        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor digite uma opção válida i, a ou l. ')
