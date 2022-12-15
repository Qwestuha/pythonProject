



def napeshatat_privetstvie(name):
    """"Print Privestvie"""
    print("Congratulitions " + name +  " wish you all the best!")


def summa(x, y):
    return x+y

#--------------------------#

print('---------------------------------')
napeshatat_privetstvie("Denis")
napeshatat_privetstvie("Zheka")

x = summa(33, 22)
print(x)

def factorial(x):
    """"Calculate Factorial of number X"""
    otvet = 1
    for i  in range(1, x+1):
        otvet = otvet * i
    return  otvet


for i in range(1, 10):
    print(str(i) + "!\t = " + str(factorial(i)))

