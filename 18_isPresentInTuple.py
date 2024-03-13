tpl = eval(input("Enter the tuple here: "))
element = int(input("Enter the element here: "))

isPresent = False
for i in range(0,len(tpl)):
    if(tpl[i] == element):
        isPresent = True
        break


print()

if(isPresent):
    print("Present")
else:
    print("Absent")
