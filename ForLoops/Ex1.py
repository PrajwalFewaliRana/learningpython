nums =[1,4,9,16,25,36,49,64,81,100]
for i in nums:
    print(i)

x = int(input("Enter the number you want to search:"))
for el in nums:
    if(el==x):
        print(x,"found at index",nums.index(x))