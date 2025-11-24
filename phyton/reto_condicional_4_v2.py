
num1 = 0
num2 = 0
# get number 1
print(" enter value to number 1:  ")
num1 = float(input())
# get num2
print(" enter value to numer 2 ")
num2 = float(input())
# print main menu
print("math menu [1]. add [2] subs. [3]mult [4]div . [5] all ", end='', flush=True)
print("press any option [1 y 5 ]")
opt = int(input())
if opt == 1:
    res = num1 + num2
    print("adittion" + str(res))
else:
    if opt == 2:
        res = num1 - num2
        print("substracction" + str(res))
    else:
        if opt == 3:
            res = num1 * num2
            print("multiplication " + str(res))
        else:
            if opt == 4:
                res = num1 / num2
                print("divition" + str(res))
            else:
                if opt == 5:
                    if num2 == 0:
                        print(" invalid option beacuse you can not divide by 0 ")
                    else:
                        print("add " + str(num1 + num2))
                        print("subs " + str(num1 + num2))
                        print(" mult " + str(num1 + num2))
                        print("div " + str(num1 + num2))
                else:
                    print("invalid options ")