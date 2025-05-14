"""
Cuidado com dados mutáveis
= - copiado o valor (imutável)
= - aponta para o mesmo valor na memória (mutável)
"""
# nome = 'Paulo'
# outro_nome = nome
# nome = 'João'

# print(nome)
# print(outro_nome)


lista_a = ['Paulo', 'Davi', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)

