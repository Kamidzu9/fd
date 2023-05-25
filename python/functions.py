#That function make factorial with number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print(result) # 

#That function make a loop with name sum and make sum of x, y
#else division x on y 
def sum(x, y):
    while x <= 1 and y <= 1:
        return x + y
        
    else:
        return x / y 

sresult = sum(10, 20)
print(sresult)

# That function write Hi, {name}!
def greet(name):
    print(f"HI, {name}!")
    
greet(input("Write your name:")) 