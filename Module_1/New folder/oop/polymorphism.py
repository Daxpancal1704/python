"In words polymorphism menas 'many forms' in programming refres to a method / function / operator with the same name that can executud one or many object and class "

"In another words class name is diffrent but method name is same"

# class Animal:
#     def __init__(self, name,age):
#         self.name=name
#         self.age=age

#     def Move(self):
#         print("Helo")       
# class Human:
#     def __init__(self,name,age):
#       self.name=name
#       self.age=age

#     def Move(self):
#         print("good") 

# a1=Animal("Alice",23)
# h1=Human("Alian",21)

# a1.Move()
# h1.Move()


"With the use of inheritance creating polymorphism"

class cla1:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def iner_method(self):
        print("Hello Good Morning,sir my slef dax panchal")


class cla(cla1):
    pass 
    
class cla2(cla1):


    def iner_method(self):
           
        print("i'm good i hope you are doing well by the way how's the possible to crack this pattern")


name=input("Hello pls , Enter your name : ")
age=int(input("Hello pls , Enter your age : "))


c1=cla1(name,age)
c2=cla2(name,age)

c1.iner_method() 
c2.iner_method()       