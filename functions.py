def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print(result)

def sum(x, y):
    while x <= 1 and y <= 1:
        return x + y
        
    else:
        return x / y 
        
print(sresult)

def greet(name):
    print(f"HI, {name}!")
    
greet(input("Write your name:"))