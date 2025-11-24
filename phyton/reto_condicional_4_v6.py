
# Apply functions with return

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
            return res
        case 2:
            res = n1 - n2
            return res
        case 3:
            res = n1 * n2
            return res
        case 4:
            if num2 > 0:
                res = n1 / n2
                return res
            else:
                print("It is not possible to divide by zero")
        case 5:
            if num2 > 0:
                return (n1 + n2), (n1 - n2), (n1 * n2), (n1 / n2)
            else:
                return (n1 + n2), (n1 - n2), (n1 * n2), "No division by zero"
        case _:
            print("Invalid option !!!")


### Main #############################################
os.system('clear')

# Get numbers
num1 = float(input("Enter value to number 1: "))
num2 = float(input("Enter value to number 2: "))
math_menu()
opt = int(input("Press any option [1 - 5]: "))

r = calc(num1, num2, opt)
print(f"Answer: {r}")


'''
if opt > 1 and opt <= 4:
    r = calc(num1, num2, opt)
    print(f"Answer: {r}")
else: # Apply for option 5
    r = calc(num1, num2, opt)
    print(f"Add: {r[0]}")
    print(f"Sub: {r[1]}")
    print(f"Mul: {r[2]}")
    print(f"Div: {r[3]}")
'''