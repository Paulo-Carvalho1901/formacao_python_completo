"""
Iterável -> str, range, etc (__iter__)
iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador
"""

# texto = 'Paulo'
# numeros = range()

# for numero in numeros:
#     print(numero)

# for letra in texto
texto = ('Paulo') # iteravel
iterador = iter(texto) # iteretor

# fluxo do for por baixo dos panos
# while True:
#     try:
#         print(next(iterador))
#     except StopIteration:
#         break
for item in texto:
    print(item)
