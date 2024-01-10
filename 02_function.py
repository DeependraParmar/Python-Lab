def factorial(n):
    ans = 1
    for i in range(2,n+1):
        ans = ans*i
    
    return ans

n = int(input("Enter the value of n: "))
print(f"Factorial of ${n} is: ", factorial(n))