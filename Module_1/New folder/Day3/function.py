"Creatin a function"

# def myfun():# creating a function
#     print("Hello")
# myfun()#calling function
# myfun()


# def fahrenheit_to_ce(fahrnheit):
#     return (fahrnheit-32)*5/9

# fahrnheit=float(input())
# print(fahrenheit_to_ce(fahrnheit))

"Return value"

# def name():
#     return "helloo good moring"

# message=name()
# print(message)
    

"---------------Function argument---------------"


# def myfun(fname,lname):
#     print(fname,"and",lname)


# myfun("dax","panchal")

"---------------Default argument------------"

def name(fname="Alice" ):
    print("Hello" , fname, "How are you , ")

name()


"------------------Keywordargument--------------"

# def my_fun(animal,name):
#     print("i have a",animal)
#     print("my",animal + " name is " , name)

# my_fun(animal="DOG",name="tomy")

"-----passing different Data type ---------"

# def myfun(number):
#     for num in number:
#         if num == 4:
#             break
#         print(num)

# numbers=[1,2,3,4,5,6]
# myfun(numbers)


def mydict(person):
    print("name",person["name"])
    print("age",person["age"])

my_dict={"name":"dax","age":23}
mydict(my_dict) 

def retun_value(x,y):
    return x+y

value=retun_value(1,2)
print(value)







"________________________________________*args function____________________________________"


# def fun(*keys):
#     print("Hello i will to learn more skill like ",keys[0])

# fun("Python","java")

"With normal argu"

# def func(age,*name):
#     for names in name:
#         print(age, names)
    
# func("hello","Dax","ram")




# def fruit(name,*colour):
#     for colours in colour:
#         print(name,colours)
# fruit("mango","red","orange","Yellow")        

    

"Enxample"

# def function(*number):
#     total=0
#     for num in number:
#         total+=num
#     return total
# print(function(10))
# print(function(10,110))


"_______**keyword_______"

# def my_fun(**kid):
#     print("name ia ",kid["lname"])
#     print("name ia ",kid["fname"])

# my_fun(lname="panchal",fname="rma")    












"__Local scope___"


# def myfun():
#     x=300

#     print(x)
# myfun()    

"-------function inside the functions----"

# def myfun():
#     x=300
#     def infun():
#         print(x)
#     infun()
# myfun()       



"---------------Global varible----------"

# x=10
# def myfun():
#     x=13
#     print(x)
# myfun()    


"-------------globl keyword-----"
# x=100
# y=2332
# def myfun():
#     global x,y
#     x=300
#     y=900
#     print(x)
# myfun()
# print(x)
# print(y)