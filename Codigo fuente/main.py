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


 
	# VARIABLES REFERENTES AL CIRCUITO
	numeroPuertas = clase2.obtenerPuertasDiferentes()
	numeroFilas = clase2.obtenerNumeroCapas()
	numeroColumnas = clase2.obtenerNumeroColumnas()

	valoresEntradaOriginal = clase2.obtenerValoresEntrada(numeroFilas, numeroColumnas)
	valoresSalidaOriginal = clase2.obtenerValoresSalida(numeroFilas, numeroColumnas)


	cromosomaOriginal = clase3.crearCromosomaInicial(numeroFilas, numeroColumnas, numeroPuertas)

	enlaces = clase3.crearEnlacesCromosoma(numeroFilas, numeroColumnas, cromosomaOriginal)


	#VARIABLES REFERENTES AL ALGORITMO GENÉTICO
	LONGITUD_CROMOSOMA = numeroColumnas*numeroFilas
	POBLACION_INICIAL = clase2.seleccionarPoblacion()
	ITERACIONES_AG = clase2.seleccionarNumeroIteraciones()
	PROB_CRUCE = clase2.seleccionarProbCruce()
	PROB_MUTACION = clase2.seleccionarProbMutacion()
	PROB_GENMUT = clase2.seleccionarProbMutacionGenoma()



# EJECUCIÓN DEL CÓDIGO
def evaluaCircuito(individuo):
	puntuacion = 0
	individuo = clase3.cambiarPuertasRotas(cromosomaOriginal, individuo)
	valoresSalida = clase3.calcularSalidasDelCircuito(valoresEntradaOriginal, individuo, enlaces)
	puntuacion = clase3.diferenciaEntre(valoresSalida, valoresSalidaOriginal)*100 + clase3.diferenciaEntre(individuo, cromosomaOriginal)
#	print("EVALUACIÓN: "+str(puntuacion))
	return (puntuacion,)




def generaGenetico():

	creator.create("FitnessMin", base.Fitness, weights=(-1,)) #Es -1 porque queremos minimizar.
	creator.create("Individuo", list, fitness=creator.FitnessMin)  #Hacemos que la fitness sea el FitnessMin
	toolbox1 = base.Toolbox()
	toolbox1.register("attr_int",random.randint, 1, numeroPuertas-1)#Este atributo es cada casilla del cromosoma, queremos que sea un INT entre [0, NºPuertasLógicasDisponibles-1
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
	print("CROMOSOMA ORIGINAL: "+str(cromosomaOriginal))
	print("EL MEJOR INDIVIDUO ENCONTRADO ES EL SIGUIENTE:\n\n"+str(clase3.imprimeFormatoCircuito(ganador, numeroFilas, numeroColumnas)))
	print("Numéricamente sería: "+str(ganador))
	print('Individuo con fitness: '+str(evaluaCircuito(ganador)[0])+"\n\n")
	print("VALORES DE ENTRADA = "+str(valoresEntradaOriginal))
	print("VALORES DE SALIDA = "+str(valoresSalidaOriginal))

	
	

generaGenetico()