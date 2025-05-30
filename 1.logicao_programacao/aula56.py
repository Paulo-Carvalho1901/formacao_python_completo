"""
split e join com list e str
split - divide uma string
join - uma uma string
"""
frase = 'Olha só que, coisa intessante   '
lista_frase_cruas = frase.split(',')


lista_de_palavras = []
for i, frase in enumerate(lista_frase_cruas):
    lista_de_palavras.append(lista_frase_cruas[i].strip())


# print(lista_frase_cruas)
# print(lista_de_palavras)

frases_unidas = '-'.join(lista_de_palavras)
print(frases_unidas)
