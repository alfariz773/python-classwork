from abc import ABC, abstractmethod 
from datetime import datetime

class user(ABC):
    def __init__(self,name,yearjoined):
        self.name=name
        self.yearjoined=yearjoined
    
    def years_platform(self):
        current_year=2025
        return current_year - self.yearjoined
    
    @abstractmethod
    
    def role(self):
        pass
    
    def __str__(self):
        return f"{self.name} ({self.role()}) has been using the platform for {self.years_platform()} years."
        
        
class coustomer(user):
    def role(self):
        return "coustomer"
    
class vendor(user):
    def role(self):
        return "vendor"
    


cus= coustomer("jude",2014)
ven= vendor("salman",2020)

print(cus)
print(ven)
