"""
Intrudção ao try/except
try -> tentar executar o código
except -> acorreu algum erro ao tentar executar
"""
numero_str = input('Vou dobrar um número que você digitar: ')


try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro do {numero_str} é {numero_float * 2}')
except:
    print('Isso não é um número.')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro do {numero_str} é {numero_float * 2} ')
# else:
#     print('Isso não é um número.')