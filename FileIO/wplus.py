f= open("wplus.txt","w+") #w+ open files for read and write but clear the file before
print(f.read()) #this clear the file
f.write("this is written file")
f.close()