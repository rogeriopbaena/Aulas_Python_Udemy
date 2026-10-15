
"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

# Aqui vamos simular um radar de velocidade, 
# o carro passa por um radar e se ele estiver acima da velocidade máxima, 
# ele é multado. E para isso vamos utilizar o if/else, 
# mas vamos fazer de uma forma que não seja ruim, ou seja, 
# vamos utilizar variáveis para armazenar as condições e depois 
# vamos utilizar essas variáveis no if/else.
# Só foi utlilizado if/else para mostrar a mensagem de que o carro foi 
# multado ou não, mas na vida real, o radar iria registrar a multa 
# e enviar para o órgão de trânsito

velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('carro multado em radar 1')