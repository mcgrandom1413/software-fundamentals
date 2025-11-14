Algoritmo Lanzar_Dados_Par_De_Seis
	
    Definir dado1 Como Entero 
	Definir  dado2 Como Entero
	Definir numero_lanzamientos  Como Entero
	Definir  i Como Entero
	
    Definir iniciar Como Caracter
    
    Escribir "Presiona ENTER para iniciar"
    Leer iniciar
    
    Escribir "¿Cuántas veces quieres tirar los dados?"
    Leer numero_lanzamientos
    
    Escribir "Iniciando...", numero_lanzamientos, " veces..."
    
    Para i <- 1 Hasta numero_lanzamientos Con Paso 1 Hacer
        dado1 <- Aleatorio(1,6)
        dado2 <- Aleatorio(1,6)
        
        Escribir "Lanzamiento ", i, ": ", dado1, " y ", dado2
        
        Si dado1 = 6 Y dado2 = 6 Entonces
            Escribir "¡ OH ! Par de seis obtenido! Fin del juego ????"
            i <- numero_lanzamientos   // Rompe el ciclo
        FinSi
    FinPara
FinAlgoritmo
