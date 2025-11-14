
	algoritmo Lanzar_Dado_Contar_Numeros
		Definir n Como Entero
		Definir  i Como Entero
		Definir dado Como Entero
		escribir "presionar enter para iniciar"
		leer iniciar
		Definir c1, c2, c3, c4, c5, c6 Como Entero
		c1<- 0
		c2 <- 0
		c3 <- 0
		c4 <- 0
		c5 <- 0
		c6 <- 0
		
		
		Escribir "¿Cuántas veces deseas lanzar el dado?"
		Leer n
		
		Para i <- 1 Hasta n Con Paso 1 Hacer
			dado <- Aleatorio(1,6)
			Segun dado Hacer
				1: c1 <- c1 + 1
				2: c2 <- c2 + 1
				3: c3 <- c3 + 1
				4: c4 <- c4 + 1
				5: c5 <- c5 + 1
				6: c6 <- c6 + 1
			FinSegun
		FinPara
		
		Escribir "Resultados:"
		Escribir "1 salió ", c1, " veces"
		Escribir "2 salió ", c2, " veces"
		Escribir "3 salió ", c3, " veces"
		Escribir "4 salió ", c4, " veces"
		Escribir "5 salió ", c5, " veces"
		Escribir "6 salió ", c6, " veces"
		
		Para i <- 1 Hasta n Con Paso 1 Hacer
			dado <- Aleatorio(1,6)
			Segun dado Hacer
				1: c1 <- c1 + 1
				2: c2 <- c2 + 1
				3: c3 <- c3 + 1
				4: c4 <- c4 + 1
				5: c5 <- c5 + 1
				6: c6 <- c6 + 1
			FinSegun
		FinPara
	
FinAlgoritmo
