Algoritmo Dados_Par_De_Seis
    Definir dado1 Como Entero
	Definir  dado2  Como Entero
	Definir impares Como Entero
	Definir  pares Como Entero
	Definir i Como Entero
    Definir iniciar Como Cadena
    
    Escribir "Presionar  ---Enter--- para iniciar"
    Leer iniciar
    
    Escribir "¿Cuántas veces quieres tirar los dados?"
    Leer numero_lanzamientos
    
    Escribir "Iniciando...", numero_lanzamientos, " veces..."
    
    Para i <- 1 Hasta numero_lanzamientos Con Paso 1 Hacer
        dado1 <- Aleatorio(1,6)
        dado2 <- Aleatorio(1,6)
        
        Escribir "Lanzamiento ", i, ": ", dado1, " y ", dado2
		
    
		si dado1  mod 2 = 0 entonces 
			pares <- pares +1
			sino 
				impares <- impares +1
				
			fin si
			
			si dado2  mod 2 = 0 entonces 
				pares <- pares +1
			sino 
				impares <- impares +1
				
				
			FinSi
            fin para
	
			Escribir "Fin de los lanzamientos."
			Escribir "Total de números pares: ", pares
			Escribir "Total de números impares: ", impares
FinAlgoritmo
