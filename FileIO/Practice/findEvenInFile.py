# count =0
# with open("numbers.txt","r") as f:
#     data = f.read()
#     numbs = data.split(",") #converting the data into list
#     for val in numbs:
#         if int(val)%2==0:
#             count +=1
# print(count)


#another method without using split
with open("numbers.txt","r") as f:
    data = f.read()
    numbs =""
    count =0
    for i in range(len(data)):
        if(data[i] == ","):
            if(int(numbs)%2==0):
                count+=1
            numbs =""
        else:
            numbs+= data[i]
    print("even number occured",count,"times")