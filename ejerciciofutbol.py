pg = int(input('ingrese numero de partidos ganados: '))
pe = int (input('ingrese numero de partidos empatados: '))
pp = int(input('ingrese numero de partidos perdidos: '))

ppg = pg*3
ppe = pe*1
ppp = pp*0

pf = ppg+ppe+ppp

print('Puntuaje final: ', pf)