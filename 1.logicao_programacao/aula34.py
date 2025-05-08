"""
Repetição
while (enquanto)
Executar uma ação enqunto uma condição for verdadeira
Loop infinito quando um código não tem fim 
"""
condicao = True

while condicao:
    nome = input(f'Qual é seu nome: ')
    print(f'Seu nome é {nome}')

    # criando condição de para do laço
    if nome == 'sair':
        break
print('ACABOU!')