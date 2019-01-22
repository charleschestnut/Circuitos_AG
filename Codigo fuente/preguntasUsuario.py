


################################
# NÚMERO DE PUERTAS DIFERENTES #
################################

def obtenerPuertasDiferentes():
	#Pedimos al usuario que introduzca el número de puertas diferentes que
	#quiere implementar en el circuito, serán un mínimo de 6 y un máximo de 8 incluyendo "la puerta rota"
	print("\n Introduzca el número de puertas que quiere emplear. El mínimo serán seis: \n 0. Puerta rota. \n  1.OR \n 2.AND \n 3.NOT \n 4.NAND \n 5.XOR. \n Existe la posibilidad de introducir: \n 6.BUFFER/YES \n 7.XNOR.\n 8.NOR.\n")
	numPuertas = solicitarNumeroAlUsuario(2,9)

	#numPuertas = estaEntre(2, 8, numPuertas)

	return(numPuertas)



###################
# NÚMERO DE CAPAS #
###################

def obtenerNumeroCapas():
	
	print("\n Introduzca el número de capas que quiere en su circuito, debe ser un mínimo de 3 y tiene como máximo 20.\n")
	numFilas = solicitarNumeroAlUsuario(3, 20)
	#numFilas = estaEntre(3, 20, numFilas)
	
	return(numFilas)



######################
# NÚMERO DE COLUMNAS #
######################

def obtenerNumeroColumnas():

	print("\n Introduzca el número de puertas que quiere en cada capa, debe ser un mínimo de 3 y tiene como máximo 10.\n")
	numColumnas = solicitarNumeroAlUsuario(3, 10)
	#numColumnas = estaEntre(3, 10, numColumnas)

	return(numColumnas)



######################
# VALORES DE ENTRADA #
######################

def obtenerValoresEntrada(intFilas, intColumnas):
	valoresEntrada= []
	i = 0
	while i < intColumnas:
		print("\n Introduzca valor de entrada que quiere tener en la posición ["+str(i)+"]. Debe ser 0 ó 1.\n")
		valor = solicitarNumeroAlUsuario(0, 1)
		#valor = estaEntre(0, 1, valor)
		valoresEntrada.append(valor)
		i = i+1
	return(valoresEntrada)



#####################
# VALORES DE SALIDA #
#####################

def obtenerValoresSalida(intFilas, intColumnas):
	valoresSalida= []
	i = 0
	while i < intColumnas:
		print("\n Introduzca valor de salida que quiere tener en la posición ["+str(i)+"]. Debe ser 0 ó 1.\n")
		valor = solicitarNumeroAlUsuario(0, 1)
		valoresSalida.append(int(valor))
		i = i+1
	return(valoresSalida)






#######################
# NÚMERO DE POBLACIÓN #
#######################

def seleccionarPoblacion():
	print("Introduzca el número de poblacion que quiere para el algoritmo genético. El mínimo permitido será una población de 100 y un máximo de 5000. \n")
	poblacion = solicitarNumeroAlUsuario(100, 5000)
	
	return(poblacion)



######################
# NÚMERO ITERACIONES #
######################

def seleccionarNumeroIteraciones():
	print("Introduzca el número de iteraciones que quiere para el algoritmo genético. El mínimo permitido será iteraciones de 100 y un máximo de 1000. \n")
	iteraciones = solicitarNumeroAlUsuario(100, 1000)

	return(iteraciones)



#########################
# PROBABILIDAD DE CRUCE #
#########################


def seleccionarProbCruce():
	print("Introduzca la probabilidad de cruce que quiere para el algoritmo genético. El mínimo permitido será un porcentaje de 30% y un máximo de 99%.\n")
	probCruce = solicitarNumeroAlUsuario(30, 99)

	return(probCruce/100)



############################
# PROBABILIDAD DE MUTACIÓN #
############################

def seleccionarProbMutacion():
	print("Introduzca la probabilidad de mutacion que quiere para el algoritmo genético. El mínimo permitido será un porcentaje de 30% y un máximo de 99%. \n")
	probMutacion = solicitarNumeroAlUsuario(30, 99)

	return(probMutacion/100)



###################################
# PROBABILIDAD DE MUTACIÓN GENOMA #
###################################

def seleccionarProbMutacionGenoma():
	print("Introduzca la probabilidad de mutacion del genoma que quiere para el algoritmo genético. El mínimo permitido será un porcentaje de 30% y un máximo de 99%. \n")
	probMutacionG = solicitarNumeroAlUsuario(30, 99)

	return(probMutacionG/100)


def solicitarNumeroAlUsuario(inicio, final):
	while 1:
		valor = input("Introduzca el valor solicitado correctamente. Debe estar entre "+str(inicio)+" y "+str(final)+". \n")
		while valor==None or not valor.strip().isdigit():
			
			print("\n Ha introducido: "+valor+", que no es un número. \n")
			valor = input("Por favor, introduzca el número solicitado. \n")

		else: 
			valor = int(valor.strip())
			if inicio <= valor <= final:
				return valor









