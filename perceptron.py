###################
###Julian Mendez###
####03/07/2017#####
###PERCEPTRON RNA##
###################

UMBRAL = 0.2
APRENDIZAJE = 0.3
peso = 0.5
_pesos = list()

def entradas(variables):
	vector = list()
	for x in range(variables):
		n = raw_input("Ingrese la variable numero {0}:".format(x))
		vector.append(int(n))
	print("Entradas: \n")
	print vector
	print(30 * "-")
	return vector

def salida():
	n = int(raw_input("Ingrese la salida esperada: "))
	print("Salida: \n")
	print  n
	print(30 * "-")
	return n

def pesos(variables):
	for x in range(variables):
		_pesos.append(peso)
	print("Pesos Iniciales: \n")
	print _pesos
	print(30 * "-")

def gnet(_entradas,_pesos):
	resultado = 0
	pass
	for i in _entradas:
		resultado = _entradas[i] * _pesos[i] + resultado

	resultado -= UMBRAL
	print("Resultado final de la iteracion: {0}".format(resultado))
	return resultado

def criterio(_resultado):
	return 0 if _resultado <= 0 else 1


def entrenamiento(_entradas,_pesos,_salida,_criterio):
	_entrenamiento = 0
	while(_salida!=_criterio):
		_entrenamiento += 1
		print("Entrenamiento numero:{0}".format(_entrenamiento))
		for x in _entradas:
			variacion = (_criterio-_salida) * APRENDIZAJE * _entradas[x]
			_pesos[x] = _pesos[x] - variacion
			print ("Peso nuevo {0}: {1}".format(x,_pesos[x]))
		_resultado = gnet(_entradas,_pesos)
		_criterio = criterio(_resultado)


	print(30 * "-")
	print ("Entrenamiento finalizado")
	print ("Cantidad de entrenamientos {0}".format(_entrenamiento))
	print ("Pesos nuevos:")
	print _pesos


def funcion(variables,primera):
	_entradas = entradas(int(variables))
	_salida = salida()
	if primera:
		pesos(int(variables))
	_resultado = gnet(_entradas,_pesos)
	_criterio = criterio(_resultado)
	if(_criterio == _salida):
		print("\n")
		print(30 * "-")
		print ("Salida correcta")
		print(30 * "-")
	else:
		print(30 * "-")
		print("\n")
		print(30 * "-")
		print ("Salida incorrecta")
		print ("Comenzando entrenamiento")
		print(30 * "-")
		entrenamiento(_entradas,_pesos,_salida,_criterio)

def getOpcion():
	print (30 * "--")
	print (30 * "--")
	print (30 * "--")
	print ("1 - Entrenar otra posibilidad")
	print ("0 - Para salir")
	opcion = int ( raw_input('Ingrese una opcion : ') )
	return opcion

def perceptron():
	variables = raw_input("Ingresa la cantidad de variables: ")
	primera = 1
	funcion(int(variables),primera)
	primera = 0
	opcion = getOpcion()
	while opcion != 0:
		if(opcion==1):
			funcion(int(variables),primera)
			opcion = getOpcion()
	exit()

def main():
	try:
		while True:
			perceptron()
	except KeyboardInterrupt:
		print("\nTerminado")
		pass

if __name__ == "__main__":
	main()


