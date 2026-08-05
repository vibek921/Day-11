# dream = "benz" #global variable
# class Pr:
#     def __init__(self):
#         self.__brand = "toyota"

#     def car(self):
#         Vehicle_type = "2 wheeler" #Local Variable
#         print(f"brand is: {self.__brand}")

# sd = Pr()
# sd.__brand = "bmw"
# sd.car()



# from abc import ABC, abstractmethod

# class Banking(ABC):

#     @abstractmethod
#     def security(self):
#         pass

#     def database(self):
#         print("you successfully access the database")

# class Mobile(Banking):
#     def security(self):
#         print("mobile security")
#     def mobile_app(self):
#         print("launch the app")

# bank = Mobile()
# bank.security()
# bank.mobile_app()




# # __len__(self)
# class Emp:
#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll
#     def __len__(self):
#         return len(self.name)
#     def info(self):
#         print(f"name: {self.name}")
#     def __str__(self):
#         return f"hi my name is {self.name}"

#     def __add__(self, other2):
#         return f"sum: {self.roll + other2}"

# dv = Emp("vibek", 16)
# dv.info()
# print(dv)
# print(len(dv))
# print(dv + 5)


# Challene Question

from abc import ABC, abstractmethod
class LibraryItem(ABC):
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def title(self):
        return self.__title

    def author(self):
        return self.__author

    @abstractmethod
    def display(self):
        pass

    def __str__(self):
        return f"book: {self.__title}"

    def __len__(self):
        ln = len(self.__title)
        return ln

    def __add__(self, other):
        ln = len(self.title())
        ln2 = len(other.title())
        return ln + ln2

class Book(LibraryItem):
        
    def display(self):
        # print(f"book: {self.title()}")
        return f"book   : {self.title()} \nauthor  : {self.author()}"

class Magazine(LibraryItem):
    def display(self):
        # print(f"book: {self.title}")
        return f"Maazine   : {self.title()} \nauthor  : {self.author()}"
class Newspaper(LibraryItem):
    def display(self):
        return f"Newspaper  : {self.title()} \nauther   : {self.author()}"



# lib = LibraryItem()
# print(f"total title lenth: {lib + 10}")

bk = Book("history", "rajesh")
# bk.display()
print(bk.display())

bk2 = Book("asd", "sw")

print("fewfwef:", bk + bk2)
mz = Magazine("Business World", "Ramlal")
print(mz.display())

ns = Newspaper("India Times", "India")
print(ns.display())

lt = [bk, bk2, mz, ns]
print("\n print details \n")
for x in lt:
    print(x.display())
    print(len(x))