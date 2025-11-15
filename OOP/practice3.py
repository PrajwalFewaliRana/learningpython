class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
        
    def showDetails(self):
        print("Order is:",self.item,"with price of",self.price)
     
    #giving the meaning of >   
    def __gt__(self,order2):
        if self.price>order2.price:
            newPrice1=self.price
            return Order(self.item,newPrice1)
            #return self
        else:
            newPrice2 = order2.price
            return Order(self.item,newPrice2)
            #return order2
    # def __gt__(self,order2):
    #     return self.price>order2.price
        
    
o1=Order("Sampoo",300)
o2=Order("chocolate",400)
o3=o1>o2 #self>order2 passed as a parameter for that dunder func
o3.showDetails()
# print(o1>o2)