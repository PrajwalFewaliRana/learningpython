# f= open("sample.txt","w") #no such file so create it for w and a
# f.write("HEllo this is sample file created using write mode")
# f.close()

f= open('sample.txt','a')
f.write("\nI am going to append some lines tooo")
f.close()

