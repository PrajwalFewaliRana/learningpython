f= open("demo.txt","r")
# data = f.readline() #to read a lline
# data = f.read(10) # to read 10 characters including spade
line1= f.readline()
line2 = f.readline()
line3 = f.readline()
print(line1) #printing after each line shows empty line after cause there is always \n aftere each line in .txt
print(line2)
print(line3)
data = f.read()
print("no data to read",data) #no more data to read so empty space show
f.close() 


