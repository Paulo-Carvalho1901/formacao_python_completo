"""
Faça uma lista de compra com listas
o usuario deve ter a possibilidade de 
inserir, apagar, e listar valores de sua lista
Não permita que o programa quebre com 
error de índices inexistentes na lista
"""

lista = []

while True:
    # criadno condição para interação com usuário
    print('Selecione uma opção:')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    # criando estrutura de controle para as opções
    if opcao == 'i':
        print('i')
    elif opcao == 'a':
        print('a')
    elif opcao == 'l':
        print('l')
    else:
        print('Por favor digite uma opção válida. ')
    