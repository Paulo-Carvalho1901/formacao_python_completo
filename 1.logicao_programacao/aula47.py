"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta
- você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
usuário digitar uma letra, você vai conferir se a letra
digitada está na palavra secreta.
    - se a letra digitada estiver na 
    palavra secreta; exiba a letra;
    - se a letra digitada não estiver 
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu 
usuario.
"""
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numeros_tentativas = 0

while True:
    
    letra_digitada = input('Digite apenas uma letra: ')
    numeros_tentativas += 1

    # condição para usuário digitar apenas uma letra
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra_formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print()
        print('VOCÊ GANHOU! PARABÉNS!')
        print()
        print('A palavra éra:', palavra_secreta)
        print('Tentativas:', numeros_tentativas)
        letras_acertadas = ''
        numeros_tentativas = 0
