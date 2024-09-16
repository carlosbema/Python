#CONSTANTES
#Poucas condições no if

velocidade = 65 #a velocidade pode mudar
local_carro = 99 #o local do carro pode mudar

RADAR = 60 #velocide máxima do radar, valor fixo
LOCAL = 100 #local onde o radar está, valor fixo
RADAR_RANGE = 1 #range do radar, valor fixo

velocidade_acima = velocidade > RADAR
carro_multado = local_carro >= (LOCAL - RADAR_RANGE) and \
    local_carro <= (LOCAL + RADAR_RANGE)

if  carro_multado and velocidade_acima:
    print('Carro multado em radar 1')