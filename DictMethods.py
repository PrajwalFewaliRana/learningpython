info = {
    "name":"Raju",
    "sub":{
        "chem":98,
        "phy":100,
        "math":99
    },
    "age":22,
    "language":"python"
    
}


print(info.keys())
print(list(info.keys()))
print(info.items())
print(info.values())
print(info.get("name"))

# newDict = {"city":"kathmandu","ward":18}
# info.update(newDict)

# or
info.update({"city":"pokhara"})
print(info)