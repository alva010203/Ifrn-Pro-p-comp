diaI = int(input('diga um dia: '))
mesI = int(input('diga um mes: '))
diaF = int(input('diga o dia final: '))
mesF = int(input('diga o mes final: '))



if mesI > mesF or diaI > diaF :
    print('A data inicial precisar ser menor que a data final.')

if mesI == 1:
    resmesI = 31
if mesI == 2:
    resmesI = 59
if mesI == 3:
    resmesI = 90
if mesI == 4:
    resmesI = 120
if mesI == 5:
    resmesI = 151
if mesI == 6:
    resmesI = 182
if mesI == 7:
    resmesI = 213
if mesI == 8:
    resmesI = 243
if mesI == 9:
    resmesI = 274
if mesI == 10:
    resmesI = 304
if mesI == 11:
    resmesI = 334
if mesI == 12:
    resmesI = 365

if mesF == 1:
    resmesF = 31
if mesF == 2:
    resmesF = 59
if mesF == 3:
    resmesF = 90
if mesF == 4:
    resmesF = 120
if mesF == 5:
    resmesF = 151
if mesF == 6:
    resmesF = 182
if mesF == 7:
    resmesF = 213
if mesF == 8:
    resmesF = 243
if mesF == 9:
    resmesF = 274
if mesF == 10:
    resmesF = 304
if mesF == 11:
    resmesF = 334
if mesF == 12:
    resmesF = 365

resulta = resmesI + diaI
resultaf = resmesF + diaF
resposta = (resultaf - resulta) 
print (f'Se passaram {resposta} dias')