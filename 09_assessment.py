def checkSubstring(fullString, subString):
    ans = False
    list = fullString.split()

    for i in list:
        if(i == subString):
            return True

fullString = "Hello, my name is Deependra Parmar"
subString = "Deependra"

print(checkSubstring(fullString,subString))