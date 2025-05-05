# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 
#  P a u l o 
# -5-4-3-2-1

# nome = 'Paulo'
# # print(nome[1])
# # print(nome[-4])

# # IN, está?
# print('a' in nome)
# print('z' in nome)
# print('-' * 10)

# # NOT IN, não esta?
# print('Pa' not in nome)
# print('z' not in nome)
# print('0' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

