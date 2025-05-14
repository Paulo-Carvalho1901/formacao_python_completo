"""
Listas em Python
Tipo list - mutável
Suporta vários valores de qualquer tipo
conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, top, del, clear, extend +
Create Read Update Delete
Criar, ler, Alterar, apagar, = lista[i] (CRUD)
"""

#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
utilmo_valor = lista.pop(3)
print(lista, 'Rmovido', utilmo_valor)
