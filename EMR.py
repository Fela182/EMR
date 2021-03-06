# -*- coding: utf-8 -*-
#!/usr/bin/python
from datetime import datetime
class colectivo():
	def __init__(self,empresa,linea,interno):
		self.empresa=empresa
		self.linea=linea
		self.interno=interno
class viaje():
	def __init__(self,colectivo,horario,monto,saldo):
		self.empresa=colectivo.empresa
		self.linea=colectivo.linea
		self.interno=colectivo.interno
		self.horario=horario
		self.monto=monto
		self.saldo=saldo
class tarjeta():
	def __init__(self,saldo,ucolectivo,interno,uhorario,cant):
		self.saldo=saldo
		self.ucolectivo=ucolectivo
		self.uhorario=uhorario
		self.uinterno=interno
		self.cant=cant
		self.list_viajes = []
		#self.aux = viaje (0,0,0)
	def mostrarviajes(self):
		for i in self.list_viajes:
			print ("Empresa " + str (i.empresa) + "  Linea " + str(i.linea) + "  Interno " + str(i.interno) + "  $ " + str(i.monto) +  "  $ " + str(i.saldo) + "   Hora " + str(i.horario))
	def recarga(self,carga):
		if(carga<196):
			self.saldo=self.saldo+carga
		else:
			if(carga<368):
				self.saldo=self.saldo+carga+34
			else:
				self.saldo=self.saldo+carga+92
	def mostrarsaldo(self):
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

	def pagar(self,colectivo,horario):
		from datetime import datetime
		fecha_inicial = self.uhorario
		fecha_final = horario
		diferencia = fecha_final - fecha_inicial
		segundos_transcurridos = diferencia.total_seconds()
		if(colectivo.linea != self.ucolectivo and segundos_transcurridos < 3600): #transbordo otro colectivo
			if(self.saldo < 1.90):
				return False
			else:
				self.saldo=round(self.saldo-1.90,2)
				self.uhorario=fecha_final
				self.ucolectivo=colectivo.linea
				self.uinterno=colectivo.interno
				#self.viajenuevo()
				self.aux = viaje(colectivo,fecha_final,1.9,self.saldo)
				self.list_viajes.append(self.aux)
				return True
		else:
			if(self.uinterno!=colectivo.interno and segundos_transcurridos < 3600): #transbordo mismo colectivo diferente linea
				if(self.saldo < 1.90):
					return False
				else:
				
					self.saldo=round(self.saldo-1.90,2)
					self.uhorario=fecha_final
					self.ucolectivo=colectivo.linea
					self.uinterno=colectivo.interno
					#self.viajenuevo()
					self.aux = viaje(colectivo,fecha_final,1.9,self.saldo)
					self.list_viajes.append(self.aux)
					return True
			else:
				if(self.saldo < 5.75):
					return False
				else:
					self.saldo=round(self.saldo-5.75,2)
					self.uhorario=fecha_final
					self.ucolectivo=colectivo.linea
					self.uinterno=colectivo.interno
					#self.viajenuevo()
					self.aux = viaje(colectivo,fecha_final,5.75,self.saldo)
					self.list_viajes.append(self.aux)
					return True
class comun(tarjeta):
	def pagarboleto(self,colectivo,horario):
		return self.pagar(colectivo,horario)
class medio(tarjeta):
	def pagarboleto(self,colectivo,horario):
		from datetime import datetime
		fecha_inicial = self.uhorario
		fecha_final = horario
		diferencia = fecha_final - fecha_inicial
		segundos_transcurridos = diferencia.total_seconds()
		datetime.strptime("25/01/2015 15:05", "%d/%m/%Y %H:%M")
		if(fecha_final.hour > 6):
			if(colectivo.linea != self.ucolectivo and segundos_transcurridos < 3600):
				if(self.saldo < 0.96):
					return False
				else:
					self.saldo=round(self.saldo-0.96,2)
					self.uhorario=fecha_final
					self.ucolectivo=colectivo.linea
					self.uinterno=colectivo.interno
					#self.viajenuevo()
					self.aux = viaje(colectivo,fecha_final,0.96,self.saldo)
					self.list_viajes.append(self.aux)
					return True
			else:
				if(self.uinterno!=colectivo.interno and segundos_transcurridos < 3600):
					if(self.saldo < 0.96):
						return False
					else:
						self.saldo=round(self.saldo-0.96,2)
						self.uhorario=fecha_final
						self.ucolectivo=colectivo.linea
						self.uinterno=colectivo.interno
						#self.viajenuevo()
						self.aux = viaje(colectivo,fecha_final,0.96,self.saldo)
						self.list_viajes.append(self.aux)
						return True
				else:
					if(self.saldo < 2.90):
						return False
					else:
						self.saldo=round(self.saldo-2.9,2)
						self.uhorario=fecha_final
						self.ucolectivo=colectivo.linea
						self.uinterno=colectivo.interno
						#self.viajenuevo()
						self.aux = viaje(colectivo,fecha_final,2.90,self.saldo)
						self.list_viajes.append(self.aux)
						return True
		else: self.pagar(colectivo,horario)
