import random
cotação = float(input('cotação atual do dolar:'))
variação = random.uniform(-0.015,0.015)
nova_cotação= cotação * (1 + variação)
print ( f'variação simulada: {variação:.3%}')
print(f'nova_cotação:{nova_cotação: .2f}')
