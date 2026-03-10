import statistics as st
lote1 = float (input('produção do lote1:'))
lote2 = float (input('produção do lote2:'))
lote3 = float (input('produção do lote3:'))
media = st.mean ((lote1,lote2,lote3))
desvio= st.stdev((lote1,lote2,lote3))
print(f'media{media:.2f}')
print(f'desvio padrão{desvio:.2f}')
