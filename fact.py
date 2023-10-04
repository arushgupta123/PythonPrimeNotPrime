
ip = int(input("Please enter a number, will give out its factors and whether prime or not"))

def getFactors(x):
    global facts
    facts = []
    for i in range(1, x+1):
        if x % i == 0:
            facts.append(i)
    
    return facts

print(getFactors(ip))



### an expansion

y = len(facts)
print(y)

if y == 1:
    print("The number you inputed is 1, it is neither prime nor not prime")
elif y == 2:
    print("The number you sent is prime")
elif y > 2:
    print("The number is not prime")
else:
    print("There is an error either in our code or your input. Please check your input")