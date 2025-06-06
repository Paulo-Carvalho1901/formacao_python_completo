import random

for _ in range(10):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    conator_regressivo_1 = 10 # criado um contador

    resultado_digito_1 = 0 
    for digito in nove_digitos: # iterando sobre novo_digito
        resultado_digito_1 += int(digito) * conator_regressivo_1 # fzendo calculo 
        conator_regressivo_1 -= 1 # fazendo o decremento contagem regressiva
    digito_1 = (resultado_digito_1 * 10) % 11 
    digito_1 = digito_1 if digito_1 <= 9 else 0 # Operação ternária

    dez_digito = nove_digitos + str(digito_1)
    conator_regressivo_2 = 11

    resultado_digito_2 = 0
    for digito in dez_digito:
        resultado_digito_2 += int(digito) * conator_regressivo_2
        conator_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

    print(cpf_gerado_pelo_calculo)