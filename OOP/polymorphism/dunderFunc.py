class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
        
    def showNumbers(self):
        print(self.real,"i +",self.imag,"j")
      
    # def add(self,num2):
    #     newReal = self.real + num2.real
    #     newImag = self.imag +num2.real
    #     return Complex(newReal,newImag)
    def __add__(self,num2):
        newReal = self.real + num2.real
        newImag = self.imag +num2.real
        return Complex(newReal,newImag)
    def __sub__(self,num2):
        newReal = self.real - num2.real
        newImag = self.imag -num2.real
        return Complex(newReal,newImag)
        
num1= Complex(4,5)
num2 = Complex(6,7)

num3=num1+num2
num4=num2-num1
# num3 = num1.add(num2) #if we do num1+num2 it shows error that cannot unsupported operand type
                        #so we use dunder function to define the meaning of operand(+)
num1.showNumbers()
num2.showNumbers()
num3.showNumbers()
num4.showNumbers()