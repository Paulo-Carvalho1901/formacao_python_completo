"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar, caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero = input('Digite um número inteiro: ')

# if numero.isdigit():
#     numero_int = int(numero)
#     par_impar = numero_int % 2 == 0
#     par_impar_texto = 'impar'

#     if par_impar:
#         par_impar_texto = 'par'
    
#     print(f'O número {numero_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro. ')


# try:
#     numero_int = int(numero)
#     par_impar = numero_int % 2 == 0
#     par_impar_texto = 'impar'

#     if par_impar:
#         par_impar_texto = 'par'
    
#     print(f'O número {numero_int} é {par_impar_texto}')
# except:
#     print('Você não digitou um número inteiro. ')

"""
Faça um programa que pergunte a hora ao usuario e, baseando-se no horário
descrito, exiba a saudação aprorpiada EX
Bom dia, 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

# while True:
#     print('-' * 30)
#     hora = input('Digite a hora desejada: ')
#     print('-' * 30)

#     hora_int = int(hora)

#     if hora_int >= 0 and hora_int <= 11:
#         print('Bom dia.')
#     elif hora_int >= 12 and hora_int <= 17:
#         print('Boa tarde.')
#     elif hora_int >= 18 and hora_int <= 23:
#         print('Boa noite.')
#     else:
#         print('Valor inválido, tente navamente. ')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"
"""

nome = input('Digite seu nome: ')

tamanho_name = len(nome)

if tamanho_name <= 4:
    print('Seu nome é curto.')
elif tamanho_name >= 5 and tamanho_name <= 6:
    print('Seu nome é normal.')
elif tamanho_name > 6:
    print('Seu nome é grande')
