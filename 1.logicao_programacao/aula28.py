"""
Exercicios
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
se nome e idade forem digitados:
    Exiba:
    Seu nome é {nome}
    Seu nome invertido é {`nome invertido}
    Seu nome contem (ou não) espaços
    Seu nome tem {n} letras
    A primeira do seu nome é {letra}
se nada for digitado em nome ou idade:
    exiba "Desculpa você deixou campos vazios"
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome} e sua idade {idade}')
    print(nome[::-1]) # invertendo a string
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços.')
    print(len(nome))

else:
    print('Desculpa você deixou campos vazios')
 