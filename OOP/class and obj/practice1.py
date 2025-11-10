# class Student:
#     def __init__(self,name,science_marks,math_marks,computer_marks):
#         self.name= name
#         self.science_marks =science_marks
#         self.math_marks = math_marks
#         self.computer_marks = computer_marks
#     def average_marks(self):
#         total = self.science_marks+self.math_marks+self.computer_marks
#         average=total/2
#         return average

# s1 = Student("Raju",98,100,99)
# print(s1.name,s1.science_marks,s1.math_marks,s1.computer_marks)
# print("average marks is:",s1.average_marks())


class Student:
    def __init__(self,name,marks):
        self.name= name
        self.marks = marks
        
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val

        print("Hi",self.name,"This is you average marks:",sum/2)

s1= Student("Ram",[99,95,93])
s1.get_avg()