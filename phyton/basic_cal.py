#Algoritm descripcioon:
""" 
basic calc v1
# Get two numbers
# addm subs, mult, div
# print results
"""
	#2. Initialize vars and/or const (inputs)
num1 = 10
num2 = 5
#3. process
add = num1 + num2
subs = num1 - num2
mult = num1 * num2
div = num1 / num2
#3. Output without f string
print ("addition: ", add, type (add))
print  ("substraction: " ,subs, type (subs))
print ("multiplicacion:" , mult, type(mult))
print ( "division: ", div, type (div))

#output f-string
print ("/n")
print (f"addition: ", {add})
print  (f"substraction:",{subs} )
print (f"multiplicacion:" ,{mult} )
print ( f"division: ", {div})
