dream = "benz" #global variable
class Pr:
    def __init__(self):
        self.__brand = "toyota"

    def car(self):
        Vehicle_type = "2 wheeler" #Local Variable
        print(f"brand is: {self.__brand}")

sd = Pr()
sd.__brand = "bmw"
sd.car()



from abc import ABC, abstractmethod

class Banking(ABC):

    @abstractmethod
    def security(self):
        pass

    def database(self):
        print("you successfully access the database")

class Mobile(Banking):
    def security(self):
        print("mobile security")
    def mobile_app(self):
        print("launch the app")

bank = Mobile()
bank.security()
bank.mobile_app()




# __len__(self)
class Emp:
    name = "vibek"
    def __len__(self):
        return len(self.name)
    def info(self):
        print(f"name: {self.name}")
    def __str__(self):
        return f"hi my name is {self.name}"


dv = Emp()
dv.info()
print(dv)
print(len(dv))



