"__str__() method is a special method that control what is returnd when the obect is print"



# class Person:
#     def add(self,a,b):
#         return a+b

#     def mul(self,a,b):
#         return a*b


# p1=Person()
# print(p1.add(10,20))
# print(p1.mul(10,10))


# class personal:

#     def intro(self,name,age,):
#         return name ,age


# name=input("name ") 
# age=int(input("age "))

# p2=personal()
# print(p2.intro(name,age))



class dog:
    def __init__(self,name):
        self.name=name


    def __str__(self):
        return self.name 
d1=dog("German")
print(d1)

class helo:

    def __init__(self,name):
        self.name=name

    def __str__(self):
        return self.name

h1=helo("hellooo")
print(h1)       





"__repr__() control the readabl"
