import math

def primeNumber(num):
    root = int(math.sqrt(num))

    for i in range(2,root+1):
        if(num % i == 0):
            return False
    
    return True


number = int(input("Enter the number for prime check: "))

if(number == 0):
    print("0 is neither PRIME nor COMPOSITE")
elif(number < 0):
    print("Can't check for negative numbers")
else:
    if(primeNumber(number)):
        print(f"{number} is PRIME")    
    else:
        print(f"{number} is COMPOSITE")