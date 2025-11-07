f= open("rplus.txt","r+") #Hello this is for rplus -> this is the content of the file
f.write("abc") #replace the first three letters with abc -> abclo this is for rplus
print(f.read()) #reads => lo this is for rplus (since the pointer was in c )
f.close()
