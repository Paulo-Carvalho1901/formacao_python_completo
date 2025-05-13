# EXEMPLO DE ITERAÇÕES COM WHILE
# texto = 'Python'
# i = 0
# tamanho_string = len(texto)

# while i < tamanho_string:
#     print(texto[i], i)

#     i += 1

#########################################

# senha_salva = '1234'
# senha_digitada = ''
# repeticoes = 0 # fazendo as repetiçoes contando quantas iterações

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(repeticoes)
# print('Aquele laço acima pode ter repetições infinitas.')

# EXEMPLO DE ITERAÇÕES COM FOR
texto = 'python'


novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')
