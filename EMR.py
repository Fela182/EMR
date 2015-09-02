# -*- coding: utf-8 -*-
#!/usr/bin/python
from datetime import datetime
class colectivo():
	def __init__(self,empresa,linea,interno):
		self.empresa=empresa
		self.linea=linea
		self.interno=interno

class viaje():
    def __init__(self,colectivo,horario,monto):
        self.empresa=colectivo.empresa
		self.linea=colectivo.linea
		self.interno=colectivo.interno
        
        self.horario=horario
        self.monto=monto



class tarjeta():
	def __init__(self,saldo,ucolectivo,uhorario,cant):
		self.saldo=saldo
		self.ucolectivo=ucolectivo
		self.uhorario=uhorario
		self.cant=cant

	def recarga(self,carga):
		if(carga<196):
			self.saldo=self.saldo+carga
		else:
			if(carga<368):
				self.saldo=self.saldo+carga+34
			else:
				self.saldo=self.saldo+carga+92



	def saldo(self):
		return self.saldo

	def viajesrealizados(self):
		return self.cant

	def viajenuevo(self):
		self.cant=self.cant+1
		print ("cantidad de viajes")		
		print (self.cant)
		print ("ultimo bondineta")
		print (self.ucolectivo)
		print ("de time")
		print (self.uhorario)



class comun(tarjeta):
	def pagarboleto(self,colectivo):
		
		from datetime import datetime

		fecha_inicial = self.uhorario
		 
		fecha_final   = datetime.now()

		diferencia = fecha_final - fecha_inicial

		segundos_transcurridos = diferencia.total_seconds()

		if(colectivo.linea != self.ucolectivo and segundos_transcurridos < 3600):
			if(self.saldo < 1.90):
				return False
			else:
				self.saldo=self.saldo-1.90
				self.uhorario=fecha_final
				self.ucolectivo=colectivo.linea
				self.viajenuevo()
				return True
		else:
			if(self.saldo < 5.75):
				return False
			else:
				self.saldo=self.saldo-5.75
				self.saldo=self.saldo-1.90
				self.uhorario=fecha_final
				self.ucolectivo=colectivo.linea
				self.viajenuevo()
				return True

class medio(tarjeta):
	def pagarboleto(self,colectivo):
		from datetime import datetime

		fecha_inicial = self.uhorario
		 
		fecha_final   = datetime.now()

		diferencia = fecha_final - fecha_inicial

		segundos_transcurridos = diferencia.total_seconds()
		if(colectivo.linea != self.ucolectivo and segundos_transcurridos < 3600):
			if(self.saldo < 0.96):
				return False
			else:
				self.saldo=self.saldo-0.96
				self.uhorario=fecha_final
				self.ucolectivo=colectivo.linea
				self.viajenuevo()
				return True
		else:
			if(self.saldo < 2.90):
				return False
			else:
				self.saldo=self.saldo-2.90
				self.uhorario=fecha_final
				self.ucolectivo=colectivo.linea
				self.viajenuevo()
				return True



fisherton=colectivo("semtur","k",101)
centro=colectivo("semtur",144,2)

seba=comun(0,1,datetime.strptime("25/01/2015 15:05", "%d/%m/%Y %H:%M")
,0)
rolo=medio(0,144,datetime.strptime("25/01/2015 15:05", "%d/%m/%Y %H:%M")
,0)

rolo.recarga(10)
seba.recarga(196)


rolo.pagarboleto(centro)
rolo.pagarboleto(fisherton)
seba.pagarboleto(fisherton)

rolo.viajesrealizados()
