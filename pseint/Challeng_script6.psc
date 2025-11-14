ALgoritmo Lanzar_Dados_Con_Enter
    Definir dado1, dado2 Como Entero
    Definir total_tiros, suma_tiros Como Entero
    Definir total_pares, total_impares Como Entero
    Definir respuesta Como Caracter
    
    total_tiros <- 0
    suma_tiros <- 0
    total_pares <- 0
    total_impares <- 0
    
    respuesta <- "S"
	
    escribir "  Presionar enter para iniciar  "
	leer iniciar
	
    Mientras respuesta = "S" Hacer
        
        Escribir ""
        Escribir " Presionar ENTER para lanzar los dados... "
        Leer  enter// solo ENTER
        
        // Lanzar dados
        dado1 <- Aleatorio(1,6)
        dado2 <- Aleatorio(1,6)
        Escribir "Resultado: ", dado1, " y ", dado2
        
        total_tiros <- total_tiros + 1
        suma_tiros <- suma_tiros + dado1 + dado2
        
        Si ((dado1 + dado2) % 2 = 0) Entonces
            total_pares <- total_pares + 1
        Sino
            total_impares <- total_impares + 1
        FinSi
        
        // --- VALIDAR RESPUESTA ---
        Repetir
            Escribir "¿Desea volver a lanzar? (S/N): "
            Leer respuesta
            respuesta <- Mayusculas(respuesta)
            
            // Convertir "SI" a "S"
            Si respuesta = "SI" Entonces
                respuesta <- "S"
            FinSi
            
            // Convertir "NO" a "N"
            Si respuesta = "NO" Entonces
                respuesta <- "N"
            FinSi
            
        Hasta Que respuesta = "S" O respuesta = "N"
        
    FinMientras
	
    Escribir "           REPORTE              "
    Escribir "Total de tiros efectuados: ", total_tiros
    Escribir "Suma total de los tiros: ", suma_tiros
    Escribir "Total de pares generados: ", total_pares
    Escribir "Total de impares generados: ", total_impares
    Escribir "--------------------------------"
	
FinAlgoritmo
