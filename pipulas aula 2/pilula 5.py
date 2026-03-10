import locale
locale.setlocale(locale.LC_ALL,'pt_BR.UFF-8')
r1 = float(input('receita1'))
r2 = float(input('receita2'))
r3 = float(input('receita3'))
total=r1+r2+r3
print(f'mes1 {locale.currency(r1,grouping=True)}')
print(f'mes2 {locale.currency(r1,grouping=True)}')
print(f'mes3 {locale.currency(r1,grouping=True)}')
print(f'total {locale.currency(r1,grouping=True)}')

