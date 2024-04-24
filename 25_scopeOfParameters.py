def func():
    """this is func"""
    x = 10
    print("x is: ", x)

x = 20
func()

print(func.__doc__)
print("global x is: ", x)