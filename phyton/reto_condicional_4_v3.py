import os

os.system('clear')
# Initilize variables or constants
num1 = 0
#num2 = 0
#res = 0

# Get number 1
num1 = float(input("Enter value to number 1: "))

# Get number 2
num2 = float(input("Enter value to number 2: "))

# Print math menu
print('''Math menu:
      [1]. Add
      [2]. Subs
      [3]. Mult
      [4]. Div
      [5]. All
''')

opt = int(input("Press any option [1 - 5]: "))

if opt == 1:
    res = num1 + num2
    print("Addition: " + str(res))
elif opt == 2:
    res = num1 - num2
    print("Substraction: " + str(res))
elif opt == 3:
    res = num1 * num2
    print("Multiplication: " + str(res))
elif opt == 4:
    if num2 > 0:
        res = num1 / num2
        print("Division: " + str(res))
    else:
        print("It is not possible to divide by zero")
elif opt == 5:
    print("Add: " + str(num1 + num2))
    print("Subs: " + str(num1 - num2))
    print("Mult: " + str(num1 * num2))
    if num2 > 0:
        print("Division: " + (num1 / num2))
    else:
        print("It is not possible to divide by zero")
else:
    print("Invalid option !!!")