def performOperations():
    lst = eval(input("Enter the list: "))

    print()
    print("List looks like this: ", lst)

    print()
    print("Now append an integer value: ", lst.append(int(input())))

    print()
    print("List looks like this: ", lst)

    print()
    print("Now sorting the list...")
    lst.sort()

    print()
    print("List looks like this: ", lst)



# performOperations()


lst1 = [1,2,3,4,5,6]
length = len(lst1)
# temp = lst1[0]
# lst1[0] = lst1[length-1]
# lst1[length-1] = temp

# index1 = int(input("Enter the first index: "))
# index2 = int(input("Enter the second index: "))

# lst1[0],lst1[length-1] = lst1[length-1],lst1[0]
# lst1[index1],lst1[index2] = lst1[index2],lst1[index1]


count = lst1.count(5)
if count>0:
    print("true")
else:
    print("false")