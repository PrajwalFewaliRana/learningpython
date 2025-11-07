#from the practice.txt replace java with python
with open("practice.txt","r") as f:
    data = f.read()
    newData = data.replace("Java","python")
with open("practice.txt","w") as f:
    f.write(newData)