class A:
    varA = "Welcome to class A\n"

class B:
    varB = "Welcome to class B\n"
    
class C(A,B):
    varC = "Welcome to class C"
    
c= C()
print(c.varA,c.varB,c.varC)