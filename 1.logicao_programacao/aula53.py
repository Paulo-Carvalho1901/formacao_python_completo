# enumerate - enumera iteráveis (índices)

lista = ['Meria', 'Helena', 'Luiz']
lista.append('João')

# for item in enumerate(lista):
#     indice, nome = item # fazendo o desempacotamento 
#     print(indice, nome)

# for item in enumerate(lista):
# print(next(lista_enumerada))
#     print(item)


for indice, nome in enumerate(lista):
    print(indice, nome)

# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')

