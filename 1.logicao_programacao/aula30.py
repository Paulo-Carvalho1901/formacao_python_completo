"""
CONSTANTE = "Variável que não vão mudar
muitas condições na mesmo if (ruin)
    <- Contagem de complexidade (ruin)
"""

velocidade = 61 # Velocidade atual do carro
local_carro = 100 # Local em que o carro esta na estrada

RODAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RODAR_RANGE = 1 # A distância onde o radar pega

velocidade_carro_passou_rodar_1 = velocidade > RODAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RODAR_RANGE) and \
    local_carro <= (LOCAL_1 + RODAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_rodar_1

if velocidade_carro_passou_rodar_1:
   print('Velocidade do carro passou do radar 1.')

if carro_passou_radar_1:
    print('Carro passou no radar 1.')

if carro_multado_radar_1:
    print('Carro multado em radar 1')
