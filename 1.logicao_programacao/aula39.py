"""
Iterando string com while
"""
     
nome = 'Paulo Carvalho' # iterável

# print(nome)
# print(tamanho_str)
# print(nome[3])

indice = 0 # criando uma indice 0
novo_nome = '' # criando uma variável novo_nome
while indice < len(nome): # aqui enquanto o indice for menor que o tamanho da string
    letra = nome[indice] # aqui criei uma varia letra que recebe cada letra na string uma a uma e salva dentro dela
    novo_nome += f'*{letra}' # aqui nesse trecho acontece acumulaçao da variável vazia novo_nome com operador de atribuição
    indice += 1 # aqui soma o indice mais ele mesmo para não ter um loop infinito

novo_nome += '*'
print(novo_nome) # imprimindo o resultado
