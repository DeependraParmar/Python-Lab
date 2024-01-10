def greaterOfThree(a,b,c):
    if(a>b and a>c):
        print("Greatest number is a: ", a)

    elif (b>c and b>a):
        print("Greatest number is b: ", b)

    else:   
        print("Greatest number is c: ", c)


a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

print()
greaterOfThree(a,b,c)