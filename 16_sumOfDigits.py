def provideDigits(num):
    result = []
    while(num != 0):
        rem = num%10
        result.append(int(rem))
        num = num / 10
    
    return result

# ____________________________________________________________

lst = eval(input("Enter the list here: "))
result = []


for i in lst:
    sum = 0
    digits = provideDigits(i)

    for j in digits:
        sum = sum + j

    result.append(int(sum))

print("Answer is: ", result)