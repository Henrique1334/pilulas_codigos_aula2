import math 
#leituras
assinantes= int(input('digite a qntd de assinantes'))
mensalidade= float(input('digite o valor da mensalidade'))
taxa = float(input('digite a taxa de crescimento mensal %'))
meses = int (input('digite a qntd de meses de projecão'))
assinantes_finais = assinantes * math.pow((1+taxa),meses)
receita_final = assinantes_finais * mensalidade
#saida
print(f"assinantes estimados:  {assinantes_finais:.0f}")
print(f'receita estimada R${receita_final:.2f}') 

