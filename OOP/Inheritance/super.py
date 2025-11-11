class School:
    def __init__(self,name,address):
        self.name = name
        self.address= address
    def something(self):
        print("We study here")
class Subject(School):
    def __init__(self,subject,name,address):
        self.subject = subject
        super().__init__(name,address) #calling the parent constructor
        super().something()

c1= Subject("science","Global","kathmandu")
print(c1.name)
print(c1.address)
print(c1.subject)