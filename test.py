import EMR
from datetime import datetime

	
k=EMR.colectivo("semtur","k",125)
centro=EMR.colectivo("Rosario Bus",144,1)
centros=EMR.colectivo("Rosario Bus",144,2)



def test_recargar():
    seba=EMR.comun(0,1,0,datetime.strptime("25/01/2015 15:05", "%d/%m/%Y %H:%M"),0)
    rolo=EMR.medio(0,144,0,datetime.strptime("25/01/2015 15:05", "%d/%m/%Y %H:%M"),0)
    fela=EMR.comun(0,115,0,datetime.strptime("25/01/2015 15:05", "%d/%m/%Y %H:%M"),0)
    seba.recarga(196)
    assert(seba.mostrarsaldo()==230)
    fela.recarga(10)
    assert(fela.mostrarsaldo()==10)
    rolo.recarga(368)
    assert(rolo.mostrarsaldo()==460)

def test_pagarBoleto():
    tarjeta1=EMR.comun(0,1,0,datetime.strptime("25/01/2015 15:05", "%d/%m/%Y %H:%M"),0)
    tarjeta1.recarga(20)
    tarjeta2=EMR.medio(0,144,0,datetime.strptime("25/01/2015 15:05", "%d/%m/%Y %H:%M"),0)
    tarjeta2.recarga(10)
    #que pague colectivo
    assert(tarjeta1.pagarboleto(k,datetime.strptime("25/01/2015 18:10", "%d/%m/%Y %H:%M")))
    assert(tarjeta2.pagarboleto(centro,datetime.strptime("25/01/2015 18:10", "%d/%m/%Y %H:%M")))
    
   
    #que pague dos boletos seguidos del mismo colectivo con el mismo interno
    
    tarjeta1.pagarboleto(k,datetime.strptime("25/01/2015 18:40", "%d/%m/%Y %H:%M"))
    assert(tarjeta1.mostrarsaldo()==8.50)
    tarjeta2.pagarboleto(centro,datetime.strptime("25/01/2015 18:26", "%d/%m/%Y %H:%M"))
    assert(tarjeta2.mostrarsaldo()==4.20)

def test_trasbordo():
    #caso de que pague un boleto de la misma linea pero diferente interno
    tarjeta3=EMR.comun(0,1,0,datetime.strptime("25/01/2015 15:05", "%d/%m/%Y %H:%M"),0)
    tarjeta3.recarga(20)
    tarjeta4=EMR.medio(0,144,0,datetime.strptime("25/01/2015 15:05", "%d/%m/%Y %H:%M"),0)
    tarjeta4.recarga(10)
    tarjeta3.pagarboleto(centro,datetime.strptime("25/01/2015 18:40", "%d/%m/%Y %H:%M"))
    tarjeta3.pagarboleto(centros,datetime.strptime("25/01/2015 18:55", "%d/%m/%Y %H:%M"))
    assert(tarjeta3.mostrarsaldo()==12.35)
    tarjeta4.pagarboleto(centros,datetime.strptime("25/01/2015 18:26", "%d/%m/%Y %H:%M"))
    tarjeta4.pagarboleto(centro,datetime.strptime("25/01/2015 18:40", "%d/%m/%Y %H:%M"))
    assert(tarjeta4.mostrarsaldo()==6.14)
    #caso diferente linea
    tarjeta5=EMR.comun(0,1,0,datetime.strptime("25/01/2015 15:05", "%d/%m/%Y %H:%M"),0)
    tarjeta5.recarga(20)
    tarjeta6=EMR.medio(0,144,0,datetime.strptime("25/01/2015 15:05", "%d/%m/%Y %H:%M"),0)
    tarjeta6.recarga(10)
    tarjeta5.pagarboleto(k,datetime.strptime("25/01/2015 18:40", "%d/%m/%Y %H:%M"))
    tarjeta5.pagarboleto(centros,datetime.strptime("25/01/2015 18:55", "%d/%m/%Y %H:%M"))
    assert(tarjeta5.mostrarsaldo()==12.35)
    tarjeta6.pagarboleto(k,datetime.strptime("25/01/2015 18:26", "%d/%m/%Y %H:%M"))
    tarjeta6.pagarboleto(centro,datetime.strptime("25/01/2015 18:40", "%d/%m/%Y %H:%M"))
    assert(tarjeta6.mostrarsaldo()==6.14)

def test_madrugada():
    tarjeta7=EMR.medio(0,144,0,datetime.strptime("25/01/2015 15:05", "%d/%m/%Y %H:%M"),0)
    tarjeta7.recarga(10)
    tarjeta7.pagarboleto(k,datetime.strptime("26/01/2015 04:00", "%d/%m/%Y %H:%M"))
    assert(tarjeta7.mostrarsaldo()==4.25)

def test_trasbordoMadrugada():
    tarjeta8=EMR.medio(0,144,0,datetime.strptime("25/01/2015 15:05", "%d/%m/%Y %H:%M"),0)
    tarjeta8.recarga(10)
    tarjeta8.pagarboleto(centros,datetime.strptime("26/01/2015 04:10", "%d/%m/%Y %H:%M"))
    tarjeta8.pagarboleto(centro,datetime.strptime("26/01/2015 04:20", "%d/%m/%Y %H:%M"))
    assert(tarjeta8.mostrarsaldo()==2.35)
    
test_recargar()
test_pagarBoleto()
test_trasbordo()
test_madrugada()
test_trasbordoMadrugada()
