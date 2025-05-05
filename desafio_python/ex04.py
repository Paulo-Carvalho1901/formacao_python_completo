"""
Faça um programa que leia algo pelo taclado
e mostre na tela  o seu tipo
primitivo e todos as informações possiveis 
sobre ela
"""

n_algo = input('Digite alguma coisa: ')

print('O tipo primitivo desse valor é: ', type(n_algo))
print('Esse valor não contem espaços? ', n_algo.isspace())
print('É um número? ', n_algo.isnumeric())
print('É alfabético? ', n_algo.isalpha())
print('É alnumerico? ', n_algo.isalnum())
print('Contem maiuscula? ', n_algo.isupper())
print('Contem minuscula? ', n_algo.islower())
print('Está capitalizada? ', n_algo.istitle())
