tpl = (1,2,3,4,5,6,7,8, 2.34234, "Hello there, I am Deependra", [1,2,3], (1,2,3))

print(tpl[9][0]) # first element of string
print(tpl[10][2]) # third element of array

oneTuple = (1,)
print(type(oneTuple))

# tpl[0] = "hello"


print("Total count of element 1 is: ", tpl.count(1))
print("Is 1 present in tuple: ", 1 in tpl)


print()
print()
for i in tpl:
    print(i, end=' | ')