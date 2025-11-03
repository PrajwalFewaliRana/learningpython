data = set()
data.add(1)
data.add("Hello world")
data.add(23)
data.add("hehe")
print(data)
data.add((1,2,3,4))
data.remove(1)
print(data)
print(data.pop())
data.clear()
print(data)

set1={1,2,3}
set2={3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))