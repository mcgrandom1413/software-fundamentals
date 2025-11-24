import os

os.system('clear')

# Get numbers
num1 = float(input("Enter value to number 1: "))
num2 = float(input("Enter value to number 2: "))

print('''Math menu:
      [1]. Add
      [2]. Subs
      [3]. Mult
      [4]. Div
      [5]. All
''')

opt = int(input("Press any option [1 - 5]: "))

match opt:
    case 1:
        res = num1 + num2
        print("Addition: " + str(res))
    case 2:
        res = num1 - num2
        print("Substraction: " + str(res))
    case 3:
        res = num1 * num2
        print("Multiplication: " + str(res))
    case 4:
        if num2 > 0:
            res = num1 / num2
            print("Division: " + str(res))
        else:
            print("It is not possible to divide by zero")
    case 5:
        print("Add: " + str(num1 + num2))
        print("Subs: " + str(num1 - num2))
        print("Mult: " + str(num1 * num2))
        if num2 > 0:
            print("Division: " + str(num1 / num2))
        else:
            print("It is not possible to divide by zero")
    case _:
        print("Invalid option !!!")
    