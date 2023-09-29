import math

y = int(input("Type a number to test for prime"))

def primeNot(num):
    numbers = [2, 3, 5, 7, 11, 13]
    status = ["","","","","",""]

    if num == 1:
        return "1 is neither prime nor not prime."

    for i in numbers:
        if math.fmod(num, i) == 0:
            status[numbers.index(i)] = bool(True)
        else:
            status[numbers.index(i)] = bool(False)

    for x in status:
        if x == bool(False):
            return bool(False)
        else:
            return bool(True)
        
if primeNot(y) == False:
    print("The number is prime")
elif y == 1:
    print(primeNot(y))
else:
    print("The number is not prime")
