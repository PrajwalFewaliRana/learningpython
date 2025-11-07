#doesnot clear the file but the cursor was already at the end cause 
# we need to add(append) from the last so the cursor point at last 
#so from the last we read nothing
f= open("aplus.txt","a+") 
f.write("this is appended value")
print(f.read()) 
f.close()