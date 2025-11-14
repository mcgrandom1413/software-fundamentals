Algoritmo suma_total_de_los_valores
	definir numero_lanzamientos como entero
	definir i como entero
	definir dado como entero
	definir suma_total como entero 

	suma_total <- 0;
	// escribo cuantas veces quiero tirar los dados
	Escribir " cuantas veces quieres tirar el dado ? "
	leer numero_lanzamientos
	
	//
	
	escribir "iniciando...  " , numero_lanzamientos, " lanzamientos ";
	para i <- 1 Hasta numero_lanzamientos con paso 1 hacer 
		dado <- Aleatorio(1,6);
		suma_total <- suma_total + dado;
		escribir "lazamientos " x ":" , dado ;
	FinPara
	
	escribir "fin de numero de lanzamientos"
	Escribir " la suma total de todos los valores de los dados en los lanzamientos es : " suma_total;
FinAlgoritmo
