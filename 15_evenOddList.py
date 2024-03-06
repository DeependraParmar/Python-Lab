lst = eval(input("Enter the list here: "))

evenList = [x for x in lst if x%2 == 0]
oddList = [x for x in lst if x%2 != 0]

print("Even list is: ", evenList)
print("Odd list is: ", oddList)