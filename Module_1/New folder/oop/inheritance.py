"Iheritance means one class and anothe sub class in anther way one parent class and one or more sub(child) class"

"Create a parent class"

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def parentmethd(self):
#         print(self.name,self.age)

# name=input()
# age=int(input())


# class person1(person):
#     print("This is Details")

# p1=person1(name,age)

# p1.parentmethd()



"super() it is used to access the parent class method in chlid class when those method object is not created"


"let's example"

class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(name+age)

class Dog(Animal):
    
    def __init__(self,name,age):
        super().__init__(name,age) 
        print("Hello")       

           
d1=Dog(23,23)