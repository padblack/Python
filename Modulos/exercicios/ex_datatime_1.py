from datetime import datetime
from dateutil.relativedelta import relativedelta

emprestimo = 1000000
data_emprestimo = datetime(2020, 12,20)
data_anos = relativedelta(years=5)
data_final = data_emprestimo + data_anos

datas_parcelas = []
data_parcela = data_emprestimo
contador = 0
while data_parcela < data_final:
    print(data_parcela,f' R${emprestimo/60:,.2f}' )
    data_parcela += relativedelta(months=+1)
    contador += 1
print(contador)
