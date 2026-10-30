"you can create a multiple time creating a object"
"Create a class with use of __init__(self) it is use of this method to not calld sperately it is also called when class object created "
"self parameter is a  reference to th current instat of a class"



"class properties vs object properties"
""

# class demo:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def greet(self):
#         print(f"hello Mr.{self.name}, How are you , I hope all are good,Congress for the complted your {self.age} years.")
                
# name=input("Enter Your name : ")
# age=int(input("Enter Your age : "))

# d1=demo(name,age)
# d1.greet()





















# class hello:# Creating a class with class keyword
#     x=5
#     # print(x)
# h1=hello()#class object create
# h2=hello() 
# print(h1.x)    
# print(h2.x)





# class Demo:d



# class demo:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# D1=demo("John",23)
# print(D1.name)
# print(D1.age)














# class emp:
#     def __init__(self,name,age,department):
#         self.name=name
#         self.age=age
#         self.department=department

#     def employe(self):
#         print("Emp name ",self.name)
#         print("Emp age ",self.age)
#         print("Emp departmnt ",self.department)

# name=input("Enter emp name :")
# age=int(input("Enter emp age :"))
# department=input("Entert emp departmnt : ")

# e1=emp(name,age,department)
# e1.employe()        


"Modifying class properties"


# class person:
#     lname=""

#     def __init__(self,name):
#         self.name=name

# p1=person("Linux")
# p1.age=23 # also add a new properties with value
# person.lname="Good"
# print(p1.age)
# print(p1.lname)







class person:
    fname="Dax"

    def __init__(self,name,age):
        self.name=name
        self.age=age

name=input("Entr the name :")
age=int(input("Enter the age :"))


P1=person(name,age)
P1.fname="Panchal"


print(P1.fname)