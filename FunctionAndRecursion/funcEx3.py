def factorial(n):
    fact = 1
    while n>=1:
        fact *=n
        n-=1 
    print("Factorial is",fact)
factorial(5)