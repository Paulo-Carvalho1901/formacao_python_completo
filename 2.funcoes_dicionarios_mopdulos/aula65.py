"""
Introdução às funções (def) em python
funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
elas podem receber valores para parâmetros (argumentos)
e retorna um valor especifico.
por padrão, funções python retornam None (nada)
"""

# def Print(a, b, c):
#     print('variavel1')
#     print('variavel2')
#     print('variavel3')

# def imprimir(a, b, c):
#     print(a, b, c)



# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

def saudacao(nome='Sem nome'):
    print(f'Ola {nome} seja ben vindo!')

saudacao('Paulo')
saudacao('Andreia')
saudacao('Davi')
saudacao()