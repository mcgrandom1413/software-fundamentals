# Apply functions without return

import os

# Function
def math_menu():
    print('''Math menu:
      [1]. Add
      [2]. Subs
      [3]. Mult
      [4]. Div
      [5]. All
    ''')

def calc(n1, n2, op):
    match op:
        case 1:
            res = n1 + n2
            print("Addition: " + str(res))
        case 2:
            res = n1 - n2
            print("Substraction: " + str(res))
        case 3:
            res = n1 * n2
            print("Multiplication: " + str(res))
        case 4:
            if num2 > 0:
                res = n1 / n2
                print("Division: " + str(res))
            else:
                print("It is not possible to divide by zero")
        case 5:
            print("Add: " + str(n1 + n2))
            print("Subs: " + str(n1 - n2))
            print("Mult: " + str(n1 * n2))
            if num2 > 0:
                print("Division: " + str(n1 / n2))
            else:
                print("It is not possible to divide by zero")
        case _:
            print("Invalid option !!!")


### Main #############################################
os.system('clear')

# Get numbers
num1 = float(input("Enter value to number 1: "))
num2 = float(input("Enter value to number 2: "))
math_menu()
opt = int(input("Press any option [1 - 5]: "))

calc(num1, num2, opt)
    