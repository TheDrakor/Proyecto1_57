#Proyecto #1
#----------------------------------------
lista = []
listaY = []
try:
	#----------------------------------------
	numero = input("Introduce un numero: ")
	#----------------------------------------
	for N in numero:
		lista.append(N)
	print(f"\nTu lista:\n{lista}")
	#----------------------------------------
	ParametroX = (len(lista)-1)
	ParametroXNegativo = (len(lista)* -1)
	#----------------------------------------
	def suma(x,y):
		#--------------------------------------------------------------------------------
		if ( x<ParametroXNegativo ) or ( x>len(lista)-1 ) or ( len(lista)<len(str(y)) ) :
			print("\n###ERROR 404###\n")
		#--------------------------------------------------------------------------------
		else:
			#-------------------
			for Y in str(y):
				listaY.append(Y)
			#-------------------
			a = 0
			b = 0
			c = -1
			#-------------------
			while a<len(listaY):
				#-------------------------------------
				resultado = int(lista[x+b]) + int(listaY[c])
				lista[x+b] = str(resultado)
				#-------------------------------------
				a += 1
				b -= 1
				c -= 1
			#-----------------------------------------
			listaInverse = lista[::-1]
			#------------------------------
			f = 1
			i = 0
			n = 0
			#------------------------------
			try:
				#--------------------------------------------------------------------------
				while n<len(lista):
					for l in listaInverse[i:f]:
							if int(l)>=10:
								#----------------------------------------------------------
								listaR = list(str(l))
								#----------------------------------------------------------
								res = int(listaInverse[i+1]) + int(listaR[0])
								listaInverse[i+1] = str(res)
								#----------------------------------------------------------
								listaInverse[i] = listaR[1]
								#--------------------------
								i += 1
								f += 1
							else:
								i += 1
								f += 1
					#---------------------------------
					n += 1
				#-------------------------------------
				listaNueva = listaInverse[::-1]
				print(f"\nLista Final:\n{listaNueva}")
			#---------------------------------------------------
			except IndexError:
						print("\n### Error en los datos obtenidos ###\n")
	#--------------------------------------------------------------------------------------------------------------------------------	
	suma(int(input(f"\nElige un parametro entre ({ParametroXNegativo},{ParametroX}): ")), int(input("\nDame una cantidad a sumar: ")) )
except ValueError:
	print("Error")
