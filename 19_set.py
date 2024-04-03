# set is unordered collection of data and hence cannot be accessed with indexing.

set1 = {1,2,3,4}
print(set1, " ", type(set))

print()

print(type({}))  # type of empty curly braces is dictionary

print()

emptySet = set()  # creates an empty set
print(type(emptySet))

print()

# setWithList = {1,"Hello", 1.2398439, [1,2,3]} set cannot have list

mySet = {1,2,3,4, "Memorize"}
list = [12,3,43,5,2]
mySet.update(list) # updating with list
mySet.update(('Deependra')) # updating with tuple
mySet.update("Hallowen") # updating with string
print(mySet)
print()

mySet.discard(1)
# mySet.remove(1999) remove raises an KeyError  if not available
print(mySet)