class A:
    
    def __init__(self,num,x):
        self.num=num
        self.x=x 
        
    def calculate(self):
        
        try:
            
            result=self.num/self.x
            print("Result:-",int(result))
            
        except:
            
            print("Any Number Can't Be Devided By Zero")
            
            
            
obj=A(10,2)
obj.calculate()
            
obj=A(10,0)
obj.calculate()

