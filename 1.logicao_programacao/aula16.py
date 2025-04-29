# if / elif       / else
# se / se não se  / se não 

"""
if, elif e else:
são utilizados para condições controle de fluxo condicional

em outras palavras se não for isso faça aquilo
executando apenas uma condição dos blocos
OBS: apenas quando a condição for (VERDADEIRA)

"""

entrada = input('Você quer entrar ou sair? ')

if entrada == 'entrar':
    print('Você entrou no sistema.')

    print(112345)
elif entrada == 'sair':
    print('Você saiu do sistena.')
else:
    print('Você não digitou nem encontrar nem sair.')

print('FORA DOS BLOCOS.')