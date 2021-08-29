

class Parent:
    
    var1= None
    # Protected
    _var2= None
    
    #Private
    __var3=None
    
    def __init__(self,var1,var2,var3):
        
        self.var1=var1
        self._var2=var2
        self.__var3=var3
        
    def printPublicMember(self):
        print("Var1=",self.var1)
        
    def _printProtectedMember(self):
        print("Var2=",self._var2)
        
    def __printPrivateMember(self):
        print("Var3=",self.__var3)
        
    def accessPrivateMember(self):
        self.__printPrivateMember()
        
class Child(Parent):
    
    def __init__(self,var1,var2,var3):
        Parent.__init__(self,var1,var2,var3)
        
    def display(self):
        self._printProtectedMember()
        

obj=Child(15,'Yes','Bye')
obj.printPublicMember()
obj.display()
obj.accessPrivateMember()
obj._printProtectedMember()
#obj.__printPrivateMember()  --> It gives error bcz __printPrivateMember() is private method and It can't be accesses outside the class.
print(obj.var1)
print(obj._var2)
#print(obj.__var3) --> It gives error bcz __var3 is private variable and It can't be accesses outside the class.
        
    
    
    
