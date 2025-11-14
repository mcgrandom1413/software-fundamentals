""""
      script description 
      crea una funcion que al ejecutar el programa genere dos numeros enteros aleatorios entre 1 y 1000, los sume y muestre en pantalla el resultado.
      recomendacion: hacer dos funciones para el mismo proceso
      f1: calc_add1: sin retorno
      f2: calc_add2: con retorno
"""


from random import randint

def calc_add0():
    x= randint(1, 1000)
    y= randint(1, 1000)
    add= x + y
    print(f"[f0.basic] adittion is: {add}")



def calc_add1 (x, y):
   
    add= x + y
    print (f"[f1: without return]addition is: {add}")



def calc_add2 (x, y):
   
    add= x + y
    return add

    ######################################### main
n1 = randint(1, 1000)   
n2 = randint(1, 1000)

calc_add0 ()
calc_add1 (n1, n2)
answer = calc_add2 (n1, n2)
print(f"[f2 with return]addition is: {answer}")


    
    ################################################



