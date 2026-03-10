import datetime
data_compra = input('data da compra(dd/mm/aaaa):')
meses = int(input('prazo de garantia'))
data_inicial = datetime.datetime.strptime(data_compra,"%d/%m/%y")
data_final = data_inicial + datetime.timedelta(days=meses *30)
print(f'garantia valida até{data_final.strptime{(%d/%m/%y)}')
print(f'dia da semana (data_final.strtime(%A))') )
