"Inner class is a class define in inside another class. inner class also accss the prperties and methods of the outer class "


# class Outer:
#     def __init__(self):
#         self.name="Hello Good Morning"

#     class inner:
#         def __init__(self):
#             self.name="God"

#         def myfun(slef):
#             print("Hello how are you")


# o1=Outer()
# print(o1.name)
# i1=o1.inner()
# print(i1.name)
# i1.myfun()













class Animal:
    def __init__(self):
        self.name="How are you ?"

    class Dog:
        def __init__(self):
            self.age=23    

        def fun(self):
            print("Goood")    


a1=Animal() #calling outside class object
print(a1.name)

d1=a1.Dog() # calling inner class with base class object
print(d1.age)
d1.fun()
           