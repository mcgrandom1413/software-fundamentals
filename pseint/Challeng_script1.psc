Algoritmo script1 
	
	definir dado como entero
	definir iniciar Como Caracter
	
	escribir " presionar Enter para lanzar dado. "
	leer iniciar 
	Escribir " dado lanzado correctamente "
	
	dado<- aleatorio(1,6)
	Escribir  "dice: ", dado 
	si dado MOD 2 = 0 entonces
		escribir " el numero es par "
	sino 
		escribir " el numero es impar. "
	FinSi
FinAlgoritmo
