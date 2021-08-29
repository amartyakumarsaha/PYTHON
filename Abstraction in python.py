from abc import ABC,abstractmethod     ### Python doesn't support abstraction so this abc module need to be called.

class Animal(ABC):
    @abstractmethod
    def info(self):
        pass

class Lion(Animal):
    
    def info(self):
        print("Lion lives in Jungle")
        
class Fish(Animal):
    
    def info(self):
        print("Fish lives in water")
        
class Bird(Animal):
    
    def info(self):
        print("Birds live in Tree")
        
obj_Lion=Lion()
obj_Lion.info()

obj_Fish=Fish()
obj_Fish.info()

obj_Bird=Bird()
obj_Bird.info()

## obj=Animal()  --> This will give error because object can't be created for a Abstract class.
