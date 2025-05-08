"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = 'Paulo Carvalho'
outra_variavel = f'{string[:3]}ABC{string[4:]}' 
# string[3] = 'ABC'
# print(outra_variavel)

# TUDO EM PYTHON É UM OBJETO, E TEM METODOS QUE SE PODE FAZER COM ESSE OBJETOS
# print(string.upper())
# print(string.lower())
print(string.capitalize())
print(string.zfill(30))
