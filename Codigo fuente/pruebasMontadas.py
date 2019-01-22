import importlib
import random
from deap import base, creator, tools, algorithms

#Cargamos la clase de preguntas de usuario con sus operaciones en la variable/puntero 'clase2'
spec2 =importlib.util.spec_from_file_location("obtenerPuertasDiferentes", "preguntasUsuario.py")
clase2 = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(clase2)


spec3 =importlib.util.spec_from_file_location("crearCromosomaInicial", "accionesCromosoma.py")
clase3 = importlib.util.module_from_spec(spec3)
spec3.loader.exec_module(clase3)



print("Aquí tenemos las diez pruebas mostradas en el documento ciencífico de Carlos Castaño del Castillo. Elija qué prueba desea realizar:")
ejecucion = clase2.solicitarNumeroAlUsuario(1, 10)

if ejecucion == 1:

	numeroPuertas = 8
	numeroFilas = 5
	numeroColumnas = 5

	valoresEntradaOriginal = [1,1,1,0,0,0]
	valoresSalidaOriginal = [1,0,1,0,1,0]


	cromosomaOriginal = [1,2,3,4,5,0,3,4,2,3,5,6,7,0,4,5,6,2,3,4,5,1,6,0,2]

	enlaces = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]


	#VARIABLES REFERENTES AL ALGORITMO GENÉTICO
	LONGITUD_CROMOSOMA = numeroColumnas*numeroFilas
	POBLACION_INICIAL = 200
	ITERACIONES_AG = 200
	PROB_CRUCE = 0.4
	PROB_MUTACION = 0.5
	PROB_GENMUT = 0.3

elif ejecucion==2:

	numeroPuertas = 2
	numeroFilas = 3
	numeroColumnas = 3

	valoresEntradaOriginal = [1,1,1]
	valoresSalidaOriginal = [1,1,1]


	cromosomaOriginal = [1, 2, 1, 2, 1, 2, 1, 2, 1]

	enlaces = [3, 4, 7, 6, 8, 7]


	#VARIABLES REFERENTES AL ALGORITMO GENÉTICO
	LONGITUD_CROMOSOMA = numeroColumnas*numeroFilas
	POBLACION_INICIAL = 100
	ITERACIONES_AG = 100
	PROB_CRUCE = 0.4
	PROB_MUTACION = 0.4
	PROB_GENMUT = 0.4

elif ejecucion == 3:

	numeroPuertas = 5
	numeroFilas = 5
	numeroColumnas = 5

	valoresEntradaOriginal = [1, 0, 1, 0, 1]

	valoresSalidaOriginal = [1, 1, 1, 1, 1]


	cromosomaOriginal = [1, 2, 0, 3, 4, 5, 3, 2, 1, 2, 3, 4, 1, 0, 3, 1, 3, 5, 3, 0, 1, 0, 3, 5, 4]


	enlaces = [5, 6, 10, 8, 7, 11, 13, 15, 16, 19, 18, 15, 17, 20, 22, 23, 24, 20, 21, 24]

	#VARIABLES REFERENTES AL ALGORITMO GENÉTICO
	LONGITUD_CROMOSOMA = numeroColumnas*numeroFilas
	POBLACION_INICIAL = 100
	ITERACIONES_AG = 100
	PROB_CRUCE = 0.4
	PROB_MUTACION = 0.4
	PROB_GENMUT = 0.4

elif ejecucion == 4:

	numeroPuertas = 9
	numeroFilas = 6
	numeroColumnas = 6

	valoresEntradaOriginal = [1, 0, 0, 1, 1, 1]


	valoresSalidaOriginal = [1, 1, 1, 0, 0, 0]


	cromosomaOriginal = [0, 1, 2, 3, 4, 6, 7, 8, 5, 2, 6, 9, 0, 1, 2, 3, 4, 5, 5, 6, 0, 1, 3, 2, 5, 4, 5, 6, 9, 8, 7, 4, 1, 0, 0, 0]

	enlaces = [6, 17, 15, 16, 13, 8, 12, 16, 17, 19, 20, 21, 23, 18, 18, 20, 25, 26, 24, 27, 28, 29, 30, 31, 35, 33, 34, 35, 32, 31]

	#VARIABLES REFERENTES AL ALGORITMO GENÉTICO
	LONGITUD_CROMOSOMA = numeroColumnas*numeroFilas
	POBLACION_INICIAL = 100
	ITERACIONES_AG = 100
	PROB_CRUCE = 0.4
	PROB_MUTACION = 0.4
	PROB_GENMUT = 0.4


elif ejecucion == 5:

	numeroPuertas = 5
	numeroFilas = 5
	numeroColumnas = 5

	valoresEntradaOriginal = [1, 0, 1, 0, 1]

	valoresSalidaOriginal = [1, 1, 1, 1, 1]


	cromosomaOriginal = [1, 2, 0, 3, 4, 5, 3, 2, 1, 2, 3, 4, 1, 0, 3, 1, 3, 5, 3, 0, 1, 0, 3, 5, 4]


	enlaces = [5, 6, 10, 8, 7, 11, 13, 15, 16, 19, 18, 15, 17, 20, 22, 23, 24, 20, 21, 24]

	#VARIABLES REFERENTES AL ALGORITMO GENÉTICO
	LONGITUD_CROMOSOMA = numeroColumnas*numeroFilas
	POBLACION_INICIAL = 10
	ITERACIONES_AG = 10
	PROB_CRUCE = 0.4
	PROB_MUTACION = 0.4
	PROB_GENMUT = 0.4



elif ejecucion == 6:

	numeroPuertas = 9
	numeroFilas = 6
	numeroColumnas = 6

	valoresEntradaOriginal = [1, 0, 0, 1, 1, 1]


	valoresSalidaOriginal = [1, 1, 1, 0, 0, 0]


	cromosomaOriginal = [0, 1, 2, 3, 4, 6, 7, 8, 5, 2, 6, 9, 0, 1, 2, 3, 4, 5, 5, 6, 0, 1, 3, 2, 5, 4, 5, 6, 9, 8, 7, 4, 1, 0, 0, 0]

	enlaces = [6, 17, 15, 16, 13, 8, 12, 16, 17, 19, 20, 21, 23, 18, 18, 20, 25, 26, 24, 27, 28, 29, 30, 31, 35, 33, 34, 35, 32, 31]

	#VARIABLES REFERENTES AL ALGORITMO GENÉTICO
	LONGITUD_CROMOSOMA = numeroColumnas*numeroFilas
	POBLACION_INICIAL = 100
	ITERACIONES_AG = 100
	PROB_CRUCE = 0.1
	PROB_MUTACION = 0.4
	PROB_GENMUT = 0.4


elif ejecucion == 7:

	numeroPuertas = 9
	numeroFilas = 6
	numeroColumnas = 6

	valoresEntradaOriginal = [1, 0, 0, 1, 1, 1]


	valoresSalidaOriginal = [1, 1, 1, 0, 0, 0]


	cromosomaOriginal = [0, 1, 2, 3, 4, 6, 7, 8, 5, 2, 6, 9, 0, 1, 2, 3, 4, 5, 5, 6, 0, 1, 3, 2, 5, 4, 5, 6, 9, 8, 7, 4, 1, 0, 0, 0]

	enlaces = [6, 17, 15, 16, 13, 8, 12, 16, 17, 19, 20, 21, 23, 18, 18, 20, 25, 26, 24, 27, 28, 29, 30, 31, 35, 33, 34, 35, 32, 31]

	#VARIABLES REFERENTES AL ALGORITMO GENÉTICO
	LONGITUD_CROMOSOMA = numeroColumnas*numeroFilas
	POBLACION_INICIAL = 100
	ITERACIONES_AG = 100
	PROB_CRUCE = 0.4
	PROB_MUTACION = 0.1
	PROB_GENMUT = 0.4



elif ejecucion == 8:

	numeroPuertas = 9
	numeroFilas = 6
	numeroColumnas = 6

	valoresEntradaOriginal = [1, 0, 0, 1, 1, 1]


	valoresSalidaOriginal = [1, 1, 1, 0, 0, 0]


	cromosomaOriginal = [0, 1, 2, 3, 4, 6, 7, 8, 5, 2, 6, 9, 0, 1, 2, 3, 4, 5, 5, 6, 0, 1, 3, 2, 5, 4, 5, 6, 9, 8, 7, 4, 1, 0, 0, 0]

	enlaces = [6, 17, 15, 16, 13, 8, 12, 16, 17, 19, 20, 21, 23, 18, 18, 20, 25, 26, 24, 27, 28, 29, 30, 31, 35, 33, 34, 35, 32, 31]

	#VARIABLES REFERENTES AL ALGORITMO GENÉTICO
	LONGITUD_CROMOSOMA = numeroColumnas*numeroFilas
	POBLACION_INICIAL = 100
	ITERACIONES_AG = 100
	PROB_CRUCE = 0.4
	PROB_MUTACION = 0.1
	PROB_GENMUT = 0.4


elif ejecucion == 9:

	numeroPuertas = 9
	numeroFilas = 6
	numeroColumnas = 6

	valoresEntradaOriginal = [1, 0, 0, 1, 1, 1]


	valoresSalidaOriginal = [1, 1, 1, 0, 0, 0]


	cromosomaOriginal = [0, 1, 2, 3, 4, 6, 7, 8, 5, 2, 6, 9, 0, 1, 2, 3, 4, 5, 5, 6, 0, 1, 3, 2, 5, 4, 5, 6, 9, 8, 7, 4, 1, 0, 0, 0]

	enlaces = [6, 17, 15, 16, 13, 8, 12, 16, 17, 19, 20, 21, 23, 18, 18, 20, 25, 26, 24, 27, 28, 29, 30, 31, 35, 33, 34, 35, 32, 31]

	#VARIABLES REFERENTES AL ALGORITMO GENÉTICO
	LONGITUD_CROMOSOMA = numeroColumnas*numeroFilas
	POBLACION_INICIAL = 100
	ITERACIONES_AG = 10
	PROB_CRUCE = 0.4
	PROB_MUTACION = 0.4
	PROB_GENMUT = 0.4


else: 

	numeroPuertas = 9
	numeroFilas = 20
	numeroColumnas = 10

	valoresEntradaOriginal = [1,0,1,1,1,0,1,1,1,0]
	valoresSalidaOriginal = [0,1,1,0,1,1,1,1,1,1]


	cromosomaOriginal = [0, 5, 6, 9, 7, 4, 5, 9, 6, 2, 0, 1, 4, 5, 6, 2, 0, 4, 2, 5, 0, 6, 0, 1, 2, 3, 7, 8, 9, 4, 5, 0, 2, 6, 7, 8, 1, 0, 3, 6, 5, 8, 9, 5, 3, 0, 3, 4, 8, 6, 3, 2, 1, 0, 2, 3, 9, 8, 7, 6, 4, 1, 5, 6, 8, 4, 2, 1, 7, 6, 2, 0, 1, 4, 8, 6, 0, 0, 1, 4, 5, 6, 3, 0, 1, 5, 5, 6, 3, 6, 5, 8, 7, 4, 5, 6, 9, 1, 2, 3, 0, 1, 2, 5, 9, 8, 7, 4, 5, 6, 3, 2, 1, 4, 5, 8, 9, 6, 7, 1, 4, 5, 6, 3, 7, 8, 9, 6, 2, 3, 0, 1, 4, 8, 6, 4, 7, 5, 9, 4, 6, 8, 2, 0, 1, 4, 5, 6, 3, 7, 8, 9, 4, 5, 6, 3, 2, 1, 0, 1, 4, 5, 6, 4, 8, 9, 6, 3, 0, 1, 4, 8, 6, 5, 2, 3, 7, 7, 8, 9, 4, 5, 6, 3, 2, 1, 4, 5, 6, 8, 5, 4, 2, 3, 6, 4, 7, 8, 9, 0]

	enlaces = [10, 12, 19, 27, 28, 26, 10, 13, 18, 19, 24, 39, 28, 26, 37, 35, 24, 25, 22, 23, 30, 32, 33, 34, 38, 40, 40, 41, 31, 37, 41, 42, 43, 45, 46, 48, 47, 49, 50, 51, 53, 54, 56, 58, 59, 57, 54, 52, 53, 65, 61, 63, 62, 67, 70, 74, 76, 78, 68, 69, 70, 71, 78, 79, 79, 74, 75, 80, 81, 89, 85, 86, 83, 82, 83, 84, 87, 88, 85, 86, 90, 91, 92, 94, 93, 95, 98, 99, 100, 104, 118, 117, 114, 116, 103, 104, 107, 108, 106, 105, 110, 111, 112, 116, 115, 118, 119, 114, 111, 113, 121, 122, 123, 124, 128, 139, 137, 135, 136, 129, 130, 130, 131, 134, 138, 137, 139, 133, 135, 136, 140, 141, 142, 144, 146, 145, 149, 148, 150, 153, 155, 157, 157, 159, 156, 154, 163, 165, 164, 167, 168, 169, 166, 160, 161, 162, 170, 172, 171, 170, 173, 174, 178, 179, 175, 174, 173, 171, 178, 180, 181, 184, 185, 186, 187, 186, 189, 183, 182, 181, 191, 190, 197, 198, 194, 196, 195, 193, 192, 190]


	#VARIABLES REFERENTES AL ALGORITMO GENÉTICO
	LONGITUD_CROMOSOMA = numeroColumnas*numeroFilas
	POBLACION_INICIAL = 300
	ITERACIONES_AG = 1540
	PROB_CRUCE = 0.6
	PROB_MUTACION = 0.65
	PROB_GENMUT = 0.67



# EJECUCIÓN DEL CÓDIGO
def evaluaCircuito(individuo):
	puntuacion = 0
	valoresSalida = clase3.calcularSalidasDelCircuito(valoresEntradaOriginal, individuo, enlaces)
	puntuacion = clase3.diferenciaEntre(valoresSalida, valoresSalidaOriginal)*100 + clase3.diferenciaEntre(individuo, cromosomaOriginal)
#	print("EVALUACIÓN: "+str(puntuacion))
	return (puntuacion,)




def generaGenetico():

	creator.create("FitnessMin", base.Fitness, weights=(-1,)) #Es -1 porque queremos minimizar.
	creator.create("Individuo", list, fitness=creator.FitnessMin)  #Hacemos que la fitness sea el FitnessMin
	toolbox1 = base.Toolbox()
	toolbox1.register("attr_int",random.randint, 0, numeroPuertas-1)#Este atributo es cada casilla del cromosoma, queremos que sea un INT entre [0, NºPuertasLógicasDisponibles-1
	toolbox1.register("individuo",tools.initRepeat,creator.Individuo,toolbox1.attr_int,n=LONGITUD_CROMOSOMA)
	toolbox1.register('poblacion',tools.initRepeat,container=list,func=toolbox1.individuo,n=POBLACION_INICIAL)
	toolbox1.register('evaluate',evaluaCircuito)
	toolbox1.register('mate',tools.cxOnePoint)
	toolbox1.register('mutate',tools.mutUniformInt,low=0,up=numeroPuertas-1,indpb=PROB_GENMUT)#La mutación hace que cambia un el valor del individuo entre 0 y nº puertas -1.
	toolbox1.register('select',tools.selTournament,tournsize=3)
	
    
	salon_fama1 = tools.HallOfFame(1)
	random.seed(12345)
       
       
	poblacion_inicial=toolbox1.poblacion()
       
	poblacion, registro = algorithms.eaSimple(poblacion_inicial,toolbox1, cxpb=PROB_CRUCE, mutpb=PROB_MUTACION, ngen=ITERACIONES_AG, halloffame=salon_fama1)


	#Elegimos el ganador   
	ganador = salon_fama1[0]
    
        
	print("\n\n\nLONGITUD DEL CROMOSOMA = "+str(LONGITUD_CROMOSOMA))
	print("NÚMERO DE PUERTAS DISPONIBLES = "+str(numeroPuertas))
	print("POBLACIÓN INCIAL = "+str(POBLACION_INICIAL))
	print("PROBABILIDAD DE CRUCE = "+str(PROB_CRUCE))
	print("PROBABILIDAD DE MUTACION = "+str(PROB_MUTACION))
	print("EL MEJOR INDIVIDUO ENCONTRADO ES EL SIGUIENTE:\n\n"+str(clase3.imprimeFormatoCircuito(ganador, numeroFilas, numeroColumnas)))
	print("Numéricamente sería: "+str(ganador))
	print('Individuo con fitness: '+str(evaluaCircuito(ganador)[0])+"\n\n")

	
	

generaGenetico()