funcion msg <- showGreeting (userName)
	escribir "hola" , userName, ",Bienvenido,"
FinFuncion




Algoritmo  function3
	Definir user_name, message como caracter
	Escribir "Enter your name: "
	Leer user_name
	
	message <- showGreeting(user_name)
	escribir message
FinAlgoritmo
