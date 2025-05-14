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
lista.append('Paulo')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(100, 5)
print(lista)
