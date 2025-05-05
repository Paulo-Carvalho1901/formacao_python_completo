"""
Formatação básica de strings
s - strings
d - int
f - float
.<número de digitos>f
x ou X - Hexadewcimal
(caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversation flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') # preechendo há esquerda
print(f'{variavel: <10}.') # preechendo há direita
print(f'{variavel: ^10}') # preechendo há centro
print(f'{1000.487888544468:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}' )
