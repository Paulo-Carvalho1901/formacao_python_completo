"""
Fatiamentos de de strings função len
 012345678
 olá mundo
-987654321

Fatiamento [i:f:p] [::]
obs: a função len retorna a qtd
de caracteres de str
"""

variavel = 'olá mundo'
print(variavel[5])
print(variavel[4:8])
print(variavel[4:])
print(variavel[0:5])
print(variavel[-8:-2])
print(variavel[0:len(variavel)])
print(variavel[0::])
print(variavel[::-1]) # Função para inverter 