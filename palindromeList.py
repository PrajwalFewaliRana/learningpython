num1 =[1,2,3,4,1]
arr = [1,"abc","abc",1]
temp2= arr.copy()
temp2.reverse()
temp1 = num1.copy()
temp1.reverse()
if(num1==temp1):
    print(num1,"is Palindrome")
else:
    print(num1,"is Not palindrome")
if(arr==temp2):
    print(arr,"is Palindrome")
else:
    print(arr,"is Not palindrome")