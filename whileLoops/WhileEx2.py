n = 0
numbers =[]
while n<11:
    numbers.append(n**2)
    n+=1
print(numbers)

n=0
x= int(input('Enter a number you want to search from above:'))
while n<len(numbers):
    if(x== numbers[n]):
        print(x,'found at index',numbers.index(x))
    n+=1