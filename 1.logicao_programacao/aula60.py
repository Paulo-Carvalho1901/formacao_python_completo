"""
Operação ternária (condicional em linha)
<valor> if <condicao> else <outro valor>
"""

# condicao = 10 == 10
# variavel = 'valor' if condicao else 'Outro valor'
# print(variavel)

digito = 9 
novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 0 else digito
print(novo_digito)
