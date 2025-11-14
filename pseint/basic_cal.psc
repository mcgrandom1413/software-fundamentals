//Algoritm descripcioon:
// basic calc v1
// Get two numbers
// addm subs, mult, div
// print results

Algoritmo basic_cal
	//1. Define vrs and/or const
	Definir num1, num2 Como Entero
	Definir add, subs, mult Como Entero
	definir div Como Real
	//2. Initialize vars and/or const
	//imputs 
	escribir "Enter number 1: " //show message to user
	leer num1 // user enter a number
	
	
	escribir "enter number 2" // show message from pc 
	leer num2
	
	
	//3. process
	add <- num1 + num2;
	subs <- num1 - num2;
	mult <- num1 * num2;
	div <- num1 / num2;
	//4. Outputs
	mostrar "addition " add;
	mostrar "substraction " subs;
	mostrar "multiplicacion" mult;
	mostrar "division " div;
FinAlgoritmo
