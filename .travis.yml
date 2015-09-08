import EMR
from datetime import datetime

	
k=EMR.colectivo("semtur","k",125)
centro=EMR.colectivo("Rosario Bus",144,1)
centros=EMR.colectivo("Rosario Bus",144,2)
seba=EMR.comun(0,1,0,datetime.strptime("25/01/2015 15:05", "%d/%m/%Y %H:%M"),0)
rolo=EMR.medio(0,144,0,datetime.strptime("25/01/2015 15:05", "%d/%m/%Y %H:%M"),0)
fela=EMR.comun(0,115,0,datetime.strptime("25/01/2015 15:05", "%d/%m/%Y %H:%M"),0)


#recarga

seba.recarga(196)
assert(seba.mostrarsaldo()==230)
fela.recarga(10)
assert(fela.mostrarsaldo()==10)
rolo.recarga(368)
assert(rolo.mostrarsaldo()==460)


#pagar boleto con y sin medio

assert(seba.pagarboleto(k,datetime.strptime("25/01/2015 18:10", "%d/%m/%Y %H:%M")))

assert(rolo.pagarboleto(centro,datetime.strptime("25/01/2015 18:10", "%d/%m/%Y %H:%M")))

assert(fela.pagarboleto(centros,datetime.strptime("25/01/2015 18:25", "%d/%m/%Y %H:%M")))


#que no pague dos boletos seguidos del mismo colectivo con el mismo interno

seba.pagarboleto(k,datetime.strptime("25/01/2015 18:40", "%d/%m/%Y %H:%M"))
assert(seba.mostrarsaldo()==218.5)

rolo.pagarboleto(centro,datetime.strptime("25/01/2015 18:26", "%d/%m/%Y %H:%M"))
assert(rolo.mostrarsaldo()==454.2)



#trasbordo

seba.pagarboleto(centro,datetime.strptime("25/01/2015 18:40", "%d/%m/%Y %H:%M"))
assert(seba.mostrarsaldo()==216.6)


rolo.pagarboleto(k,datetime.strptime("25/01/2015 18:26", "%d/%m/%Y %H:%M"))
assert(rolo.mostrarsaldo()==453.24)


#pago con medio a las 00 a 06 am

rolo.pagarboleto(k,datetime.strptime("26/01/2015 04:00", "%d/%m/%Y %H:%M"))
assert(rolo.mostrarsaldo()==447.49)

#trasbordo con medio 00 a 06 am

rolo.pagarboleto(centro,datetime.strptime("26/01/2015 04:20", "%d/%m/%Y %H:%M"))
assert(rolo.mostrarsaldo()==445.59)


