# Desenpacotamento em chamadas
# de métodos e funções
string =  'ABC'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'python', 'é', 'legal'

salas = [
    # 0
    ['Maria', 'Helena',], # 0
    # 0
    ['Elaine',], # 1
    # 0       1      2
    ['Luiz', 'João', 'Eduardo',], # 2 
]

# a, *_, c = lista
# print(a, c)

# for nome in lista:
#     print(nome, end=' ')

# print(*lista)
# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*string)


print(*salas, sep='\n')