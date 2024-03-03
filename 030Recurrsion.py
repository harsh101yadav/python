def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)
    
# print(factorial(3))
# print(factorial(4))
# print(factorial(5))


#fabonacchi

# Quick Quiz: Write a program to print the Fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

# 0 1 1 2 3 5 8....

def fabonacchi(n,a=0,b=1):
    if(n==0):
        print("done")
    else:
        print(a)
        const = a
        a = b
        b = const + b
        fabonacchi(n-1,a,b)

fabonacchi(10)