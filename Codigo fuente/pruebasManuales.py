import importlib

import random

#Cargamos la clase de preguntas de usuario con sus operaciones en la variable/puntero 'clase2'
spec2 =importlib.util.spec_from_file_location("obtenerPuertasDiferentes", "preguntasUsuario.py")
clase2 = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(clase2)


spec3 =importlib.util.spec_from_file_location("crearCromosomaInicial", "accionesCromosoma.py")
clase3 = importlib.util.module_from_spec(spec3)
spec3.loader.exec_module(clase3)




evaluaciones = []
while True:
	entrada = input("SI QUIERES CREAR UN NUEVO CIRCUITO Y SUS ENLACES PARA PROBAR LO BUENOS QUE SON RESPEECTO AL DESEADO, PULSA ENTER. SI QUIERES SALIR DE LA APLICACIÓN, ESCRIBE 'salir' y pulsa enter. \n")
	if entrada == "salir":
		break;
	
	else:
		numeroPuertas = clase2.obtenerPuertasDiferentes()
		numeroFilas = clase2.obtenerNumeroCapas()
		numeroColumnas = clase2.obtenerNumeroColumnas()

		valoresEntradaOriginal = clase2.obtenerValoresEntrada(numeroFilas, numeroColumnas)
		valoresSalidaOriginal = clase2.obtenerValoresSalida(numeroFilas, numeroColumnas)

		print("PRIMERO VAMOS A CREAR UN CROMOSOMA CON EL QUE COMPARARNOS")
		cromosoma1 = clase3.crearCromosomaInicial(numeroFilas, numeroColumnas, numeroPuertas)

		print("AHORA PROCEDEREMOS A LA CREACIÓN DE LOS ENLACES QUE HAY EN EL CIRCUITO. HE DE RECORDAR QUE LOS ENLACES ENTRE SALIDA D EUNA PUERTA Y ENTRADA DE OTRA SON INMUTABLES UNA VEZ CREADAS. ES DECIR, NO VARÍAN DE UN CROMOSOMA A OTRO PARA SU COMPARACIÓN.")
		enlaces = clase3.crearEnlacesCromosoma(numeroFilas, numeroColumnas, cromosoma1)
		
		while True:
			
			print("PROBAREMOS LA EVALUACIÓN DE NUESTRO PRIMER CROMOSOMA CON ESTE OTRO.")

			cromosoma2 = clase3.crearCromosomaInicial(numeroFilas, numeroColumnas, numeroPuertas)

			evaluacion = clase3.evaluaCircuito(cromosoma1, cromosoma2, valoresEntradaOriginal, valoresSalidaOriginal, enlaces)

			evaluaciones.append(evaluacion)

			print("===== EL RESULTADO DE LA EVALUACIÓN ES: "+str(evaluacion)+" =======")

			salir = input("Si desea reestablecer por completo todos los valores de los cromosomas o salir de la aplicación, escriba 'salir'. De lo contrario, pulse ENTER. \n")

			if salir == "salir":
				break;


print(" DURANTE EL PROCESO DE PRUEBAS MANUALES HA REALIZADO USTED: "+str(len(evaluaciones))+" EVALUACIONES. ESTOS SON SUS DIFERENTES PUNTUACIONES DE FITNESS: \n \n"+str(evaluaciones))