"Encapsulation is about protecti the data inside class "
"it menas keeping data protecting data and methods, while controlling how the data can be accessed form outside the class "

"Private property wit use of __prefix"

"in python private using double __underscore "
"Why using Encapsulation becaue data needed the protection and valiations , Flxibility, Control "



# class person:
#     def __init__(self ,name,age):
#         self.name=name
#         self.__age=age #private variable 

#     def get_access_age(self):
#         return self.__age

#     def setage(self, age):
#         if age > 0:
#             self.__age =age
#         else:
#             print("age is mut positive")

        
# p1=person("Email",23)
# print(p1.name) 
# print(p1.get_access_age())# Error occurs
# p1.setage(26)
# print(p1.get_access_age())



"'protected properties' python also hve proetectd properties with single _prefix "



# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self._age=age #  protected property


# p1=person("Linux",23)
# print(p1.name)
# print(p1._age)




class person:
    def __init__(self,name, _age ,__salary):
        self.name=name
        self._age=_age
        self.__salary=__salary

    def show(self):
            print(self.name)
            print(self._age)
            print(self.__salary)

p1=person("Dax",23,50000)

# print(p1.name)
# print(p1._age())
p1.show()