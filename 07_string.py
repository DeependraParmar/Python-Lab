first_name = "Deependra"
last_name = "Parmar"

print(first_name*3) # prints the string 3 times
print()

full_name = first_name + " " + last_name
print("Full name is: ", full_name)

print()
print("Indexing in string: ", first_name[0:10])


# reversing a string from slicing 
print()
print("Reverse of string: ", first_name[::-1])


# disjoint concatenation 
print(str(1) + "string")

print(len(first_name))
print(first_name.upper())
print(first_name.lower())

x = 100
if x==100:
    print("x is 100")
else:
    print("x is not 100")