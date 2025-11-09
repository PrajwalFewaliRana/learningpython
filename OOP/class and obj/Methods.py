class Student:
    def __init__(self,name,score):
        self.name= name
        self.score = score
    def welcome(self):
        print("welcome",self.name,".\nYOur score is",self.score)
s1 = Student("Raju",98)
s1.welcome()
# Student.welcome()=> error