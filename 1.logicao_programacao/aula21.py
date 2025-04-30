# Operador lógico 
# and (e) or (ou) not (não)
# and - Todos as condições precisam ser 
# verdadeiras.
# Se qualquer valor for considereado falso,
# a expressão inteira será avaliada naquele valor
# são considerados falsy (que você ja viu)
# 0 0.0 '' False 
# Também existe o tipo None que é 
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '1234'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

