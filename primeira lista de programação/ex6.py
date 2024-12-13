from datetime import datetime
from dateutil.relativedelta import relativedelta

sexo = input('informe o sexo (maculino/feminino): ')
data_de_nasci = input('informe a data de nascimento (DD/MM/AAAA):')
inicio_contribu = input('informe a data do inicio da contribuição (DD/MM/AAAA):')

data_de_nasci = datetime.strptime(data_de_nasci, '%d/%m/%Y')
inicio_contribu = datetime.strptime(inicio_contribu, '%d/%m/%Y')

if sexo == 'masculino' :
 idade = 65 
else:
 idade = 62

if sexo == 'masculino':
 tempode_con = 35
else: 
 tempode_con = 30


data_aposent = data_de_nasci + relativedelta(years= idade)
data_apo_contri = inicio_contribu + relativedelta(years= tempode_con)
 

print('data relativa a idade:')
print(data_aposent.strftime('%d/%m/%Y'))
print('data relativa a contribuição:')
print(data_apo_contri.strftime('%d/%m/%Y'))