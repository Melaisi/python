
"""
:author:
    Melaisi
"""
class Person(object):

    def __init__(self, _initial_age=None):
        self.age = _initial_age
        pass

    def what_am_i(self):
        if self._age < 13 :
            print("You are young...")
        elif self._age < 18:
            print("You are a teenager")
        else:
            print("You are and adult...")

        
    def year_passes(self):
        self.age+=1 
          
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,value):
        if value == 0:
            raise ValueError("Age cannot be 0")
        elif not isinstance(value,int) and not isinstance(value,float):
            raise ValueError("Age is not a number")
        elif value <0:
            raise ValueError("Age cannot be negative")
        else:
            self._age = value 