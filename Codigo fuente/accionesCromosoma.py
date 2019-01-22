import importlib

#Cargamos la clase de puertas lógicas con sus operaciones en la variable/puntero 'clase1'
spec1 =importlib.util.spec_from_file_location("pl0_broken", "accionesPuertasLogicas.py")
clase1 = importlib.util.module_from_spec(spec1)
spec1.loader.exec_module(clase1)

spec2 =importlib.util.spec_from_file_location("obtenerPuertasDiferentes", "preguntasUsuario.py")
clase2 = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(clase2)



#####  CREAR CROMOSOMA #####
def crearCromosomaInicial(filas, columnas, puertasDiferentes):
	cromosoma = []
	valorMaximo = filas*columnas
	i = 1
	j = 1
	print("A continuación vamos a empezar a definir nuestro circuito, el cual tiene "+str(filas)+" capas y "+str(columnas)+" puertas en cada una. \n Debe incluir una a una el tipo de puerta que quiere en cada posición.")
	while i <= filas:
		j = 1
		while j <= columnas:
			print("Está en la puerta lógica nº"+str(j)+" de la fila "+str(i)+".\n")
			valor = clase2.solicitarNumeroAlUsuario(0, puertasDiferentes) #Creamos un método a parte para así compromar mejor las restricciones
			cromosoma.append(valor)
			j = j+1
		i = i+1
	return cromosoma





# AQUÍ SOLICITAMOS QUE EL USUARIO ENLACE LA PUERTA ACTUAL CON OTRA. NO SE UTILIZA EN LA ÚLTIMA FILA PORQUE ESTARÁ CONECTADA CON LA SALIDA DEL CIRCUITO AUTOMÁTICAMENTE.
def crearEnlacesCromosoma(filas, columnas, cromosoma):
	enlaces = []
	print("AHORA PROCEDEREMOS A LA CREACIÓN DE LOS ENLACES QUE HAY EN EL CIRCUITO. HE DE RECORDAR QUE LOS ENLACES ENTRE SALIDA DE UNA PUERTA Y ENTRADA DE OTRA SON INMUTABLES UNA VEZ CREADAS. ES DECIR, NO VARÍAN DE UN CROMOSOMA A OTRO PARA SU COMPARACIÓN.\n")
	for idx in range(len(cromosoma)):
		if idx < columnas*(filas-1): #LO PRIMERO QUE COMPROBAMOS ES QUE LOS DE LA ÚLTIMA FILA NO PUEDEN TENER ENLACES DE SALIDA
			print("Debemos enlazar el valor de salida de la puerta nº"+str(idx)+" del circuito con la entrada de otra puerta. Recuerde que sólo puede ser con las puertas de los dos niveles inferiores.\n")
			valorEnlace = comprobarEnlaceValido(cromosoma, enlaces, idx, filas, columnas)
			enlaces.append(valorEnlace)
			print("La lista de enlaces hasta ahora es: \n"+str(enlaces))

	return enlaces



# EN ESTA FUNCIÓN COMPROBAMOS Y MOSTRAMOS AL USUARIO LAS POSIBLES CASILLAS CON LAS QUE PUEDE ENLAZAR LA PUERTA NºX INDEPENDIENTEMENTE DE SU POSICIÓN
# COMPROBANDO INCIALMENTE QUE LA PRIMERA POSICIÓN VÁLIDA ES LA PRIMERA PUERTA DEL NIVEL INFERIOR.
# TAMBIÉN QUE LA ÚLTIMA POSIBLE SERÍA LA ÚLTIMA PUERTA DEL SEGUNDO NIVEL INFERIOR. EN CASO DE QUE ÉSTE NIVEL NO EXISTA, DEBE SER LA ÚLTIMA CASILLA DEL NIVEL INFERIOR A LA PUERTA NºX.
# LA OBTENCIÓN DE LOS ÍNDICES, TANTO DE LA 1a COMO LA ÚLTIMA POSICIÓN VÁLIDA SE HAN OBTENIDO UTILIZANDO MATEMÁTICA DISCRETA
# EN CASO DE QUE LA CASILLA SELECCIONADA TENGA TODAS SUS ENTRADAS YA OCUPADAS, SOLICITAMOS AL USUARIO QUE INTENTE DE NUEVO CON OTRA PUERTA.
def comprobarEnlaceValido(cromosoma, enlaces, idx, filas, columnas):
	primeraPosicionValida, ultimaPosicionValida = 0, 0

	primeraPosicionValida = idx- (idx%columnas)+columnas
	posicionFinalSegundoNivel = primeraPosicionValida + 2*columnas-1
		
	#Comprobamos que si hay una ó dos capas más tras la capa actual del índice (idx)
	if posicionFinalSegundoNivel > filas*columnas:
		ultimaPosicionValida = primeraPosicionValida+columnas-1
		
	else:
		ultimaPosicionValida = posicionFinalSegundoNivel
	

	while 1:
		valor = clase2.solicitarNumeroAlUsuario(primeraPosicionValida, ultimaPosicionValida)

		#Comprobar que esa puerta tiene (al menos) un valor libre
			# Puertas lógicas 3 y 6 -> 1 valor de entrada
			# Puertas lógicas restantes -> Hasta 2 valores de entrada (o 1 repetido)
		if(cromosoma[valor] == 3 or cromosoma[valor] == 6) and estaEntradaSimpleDisponible(valor, enlaces):
			return valor

		elif (cromosoma[valor] != 3 and cromosoma[valor] != 6) and estaEntradaDobleDisponible(valor, enlaces):
			return valor

		else: 
			print("Esta puerta lógica ya tiene todos sus valores de entrada asignados, elija otra puerta a la que enlazar.\n")
			#Este caso se da cuando hemos solicitado el enlace con una puerta lógica y no tenía entradas
			#disponibles, por lo que volveremos a solicitar el valor.



#Comprobar que esa puerta tiene (al menos) un valor libre
# Puertas lógicas 3 y 6 -> 1 valor de entrada
def estaEntradaSimpleDisponible(valor, enlaces):
	for idx in range(len(enlaces)):

		if valor == enlaces[idx]:
			return False
	return True



#Comprobar que esa puerta tiene (al menos) un valor libre
# Puertas lógicas restantes -> Hasta 2 valores de entrada (o 1 repetido)
def estaEntradaDobleDisponible(valor, enlaces):
	contador = 0
	for idx in range(len(enlaces)):
		
		if valor == enlaces[idx]:
			contador = contador+1

		if contador==2:
			return False

	return True



# AQUÍ ENCONTRAMOS LOS MÉTODOS RELACIONADOS CON LA FUNCIÓN FITNESS #

# 0. CREAMOS UN DICCIONARIO Y UNA LISTA PARA LAS ENTRADAS DE LAS PUERTAS Y PARA LA SALIDA DEL CIRCUITO, RESPECTIVAMENTE
# 1. PARA TODAS LAS PUERTAS DEL CIRCUITO
# 1.1 SI NO ESTÁ EN LA ÚLTIMA LÍNEA -> SU SALIDA ESTÁ ENLAZADA CON ALGUNA ENTRADA, POR TANTO DEBE ESTAR EN LA LISTA DE ENLACES.
# 1.2 SI ESTÁ EN LA PRIMERA FILA -> EL VALOR DE ENTRADA QUE OBTIENE ES EL BIT POSICIONAL 'e' QUE ENTRA EN EL CIRCUITO.
# 1.3 SI NO ESTÁ EN LA PRIMERA FILA:
# 	1.3.1 BUSCAMOS QUÉ VALORES DE ENTRADA TIENE ESA PUERTA LÓGICA.
# 	1.3.2 OBTENEMOS EL VALOR DE SALIDA QUE TIENE ESA PUERTA LÓGICA.
#	1.3.3 SI NO ES LA ÚLTIMA FILA:
#		1.3.3.1 AÑADIMOS EL VALOR DE SALIDA COMO ENTRADA DE LA PUERTA CON LA QUE ESTÁ ENLAZADA USANDO UN DICCIONARIO.
#	1.3.4 EN EL OTRO CASO:
#		1.3.4.1 AÑADIMOS EL VALOR DE SALIDA DE LA PUERTA COMO VALOR DE SALIDA EN LA LISTA CREADA EN EL PUNTO 0.
# 2. DEVOLVER LAS SALIDAD DEL CIRCUITO.
def calcularSalidasDelCircuito(valoresEntrada, circuito, enlaces):
	puertasYEntradasRespectivas = {}
	salidaDelCircuito = []
	for e in range(len(circuito)):
		puertaConectada = None

		if e < len(enlaces):  #SI NO ES LA ÚLTIMA LÍNEA, TENDREMOS UNA SALIDA QUE CONECTA CON UNA PUERTA.
			puertaConectada = enlaces[e]


		if e < len(valoresEntrada): #ESTO AFECTA SÓLO A LOS DE LA PRIMERA FILA, QUE USAREMOS COMO VALORES DE ENTRADA LOS PROPIOS BITS ENTRANTES DEL CIRCUITO
			valorSalidaPuerta = calcularSalidaPuerta(circuito[e], valoresEntrada[e], None)	

		else: 
			entrada1, entrada2 = obtenerEntradasPuerta(puertasYEntradasRespectivas, e)
			valorSalidaPuerta = calcularSalidaPuerta(circuito[e], entrada1, entrada2)
			
			if e >= len(enlaces):
				salidaDelCircuito.append(valorSalidaPuerta)

		puertasYEntradasRespectivas = anadirNuevoValorSalienteComoEntrada(puertasYEntradasRespectivas, puertaConectada, valorSalidaPuerta)
	return salidaDelCircuito
	


def calcularSalidaPuerta(tipoPuerta, entrada1, entrada2):
	if tipoPuerta == 0:
		return 0

	
	elif entrada1 == None:   #SI SÓLO TIENE UN VALOR ACTIVO COMO ENTRADA TENIENDO LA POSIBILIDAD DE DOS. AMBAS ENTRADAS VALEN LO MISMO
			entrada1 = entrada2
	
	elif entrada2 == None:
			entrada2 = entrada1

	if tipoPuerta == 3:   #SI LA PUERTA ES NOT, devuelve el negado.
		return clase1.pl3_not(entrada1)
	
	elif tipoPuerta == 6:   #SI LA PUERTA ES YES/BUFFER, devuelve valor entrante directo.
		return clase1.pl6_yes(entrada1)

	elif tipoPuerta == 1:
		return clase1.pl1_or(entrada1, entrada2)

	elif tipoPuerta == 2:
		return clase1.pl2_and(entrada1, entrada2)

	elif tipoPuerta == 4:
		return clase1.pl4_nand(entrada1, entrada2)

	elif tipoPuerta == 5:
		return clase1.pl5_xor(entrada1, entrada2)

	elif tipoPuerta == 7:
		return clase1.pl7_xnor(entrada1, entrada2)

	elif tipoPuerta == 8:
		return clase1.pl8_nor(entrada1, entrada2)


	

# 1 Buscar en el diccionario la clave 'e' y devolver sus valores. 
# 1.1 Si hay cero valores, devolvemos dos 0. 
# 1.2 Si hay un valor a, devolvemos a y 0.
# 1.3 Si hay dos valores, devolvemos los dos valores.
def obtenerEntradasPuerta(diccionario, e):
	entrada1 = entrada2 = 0 
	clave = None
	for key in diccionario:
		if key == e:

			if len(diccionario[key]) == 0:
				break;
			elif len(diccionario[key]) == 1:
				entrada1 = diccionario[key][0]
				break;
			else:
				entrada1 = diccionario[key][0]
				entrada2 = diccionario[key][1]
				break;

	return entrada1, entrada2





# 1. Ver si el diccionario tiene como clave 'puertaConectada'
	# 1.1 Si no está en el diccionario:
		# 1.1.1 Crear esta nueva clave en el diccionario.
	# 1.2 Añadir 'valorSalidaPuerta' al conjunto de 'puertaConectada'.
def anadirNuevoValorSalienteComoEntrada(diccionario, puertaConectada, valorSalidaPuerta):
	if not puertaConectada in diccionario:
		diccionario[puertaConectada] = [valorSalidaPuerta]

	diccionario[puertaConectada].append(valorSalidaPuerta)
	
	return diccionario




# Es la función FITNESS: SUMATORIO DE SALIDAS DISTINTAS*100 + Nº CAMBIOS EN EL CIRCUITO. CUÁNTO MÁS ALTO SEA EL RESULTADO, PEOR SERÁ.
def evaluaCircuito(cromosomaOriginal, circuito, entrada, salidasBuenas, enlaces):
	puntuacion = 0
	circuito = cambiarPuertasRotas(cromosomaOriginal, circuito)
	valoresSalida = calcularSalidasDelCircuito(entrada, circuito, enlaces)
	puntuacion = diferenciaEntre(valoresSalida, salidasBuenas)*100 + diferenciaEntre(circuito, cromosomaOriginal)

	return puntuacion


def diferenciaEntre(lista1, lista2):
	contador = 0
	for x in range(len(lista1)):
		if lista1[x] != lista2[x]:
			contador +=1

	return contador



def imprimeFormatoCircuito(cromosoma, numeroFilas, numeroColumnas):
	impreso = ""
	for f in range(numeroFilas):
		impreso = impreso +"Capa nº"+str(f)+": ["
		for c in range(numeroColumnas):
			indice = f*numeroColumnas+c
			puerta = obtenerStringPuerta(cromosoma[indice])
			impreso = impreso + puerta
			
			if c == numeroColumnas-1:
				impreso = impreso+"]\n"
			else:
				impreso = impreso+", "
	return impreso

def obtenerStringPuerta(puerta):
	if puerta == 0:
		return "XXX"

	elif puerta == 1:
		return "OR"
	elif puerta == 2:
		return "AND"
	
	elif puerta == 3:
		return "NOT"
	
	elif puerta == 4:
		return "NAND"
	
	elif puerta == 5:
		return "XOR"
	
	elif puerta == 6:
		return "YES"
	
	elif puerta == 7:
		return "XNOR"
	
	else:
		return "NOR"


# ESTE MÉTODO SIRVE COMO "PARCHE" PARA QUE EL ALGORITMO GENÉTICO NO QUITE LAS PUERTAS ROTAS DEL CIRCUITO Y LAS SUSTITUYA POR OTRAS.
# YA QUE SE TRATA DE UNA ROTURA HARDWARE Y ES PERMAMENTE EN EL CIRCUITO. 
def cambiarPuertasRotas(original, nuevo):
	for idx in range(len(nuevo)):
		if original[idx] == 0:
			nuevo[idx] = 0

	return nuevo

