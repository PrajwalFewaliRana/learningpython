# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy= phy
#         self.chem = chem
#         self.math = math
#         self.percentage = str((phy+chem+math)/3)+"%"
        
#     #we can also use another function to update the percentage and call it after the change in marks
#     # def calcPercentage(self):
#     #     self.percentage = str((self.phy+self.chem+self.math)/3)+"%"   
# s1=Student(98,97,99)
# print(s1.percentage) #98.0%
# s1.phy=94
# # s1.calcPercentage()
# print(s1.percentage) #98.0% no update so to solve this we do either



# or we can use class methods
class Student:
    def __init__(self,phy,chem,math):
        self.phy= phy
        self.chem = chem
        self.math = math
    @property
    def Percentage(self):
       return str((self.phy+self.chem+self.math)/3)+"%"
s1=Student(98,97,99)
print(s1.Percentage)
s1.phy=94
print(s1.Percentage) 

