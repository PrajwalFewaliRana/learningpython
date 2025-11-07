with open("practice.txt","r") as f:
    data = f.read()
    if(data.find("learning") != -1):
        print("found")
    else:
        print("Not found")