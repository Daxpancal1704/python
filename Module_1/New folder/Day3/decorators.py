"Decorators use the extra behavior to a function without changing any functions code "
"Decorators name start with @Decorators_name"

# def function(func):
#     def myinner():
#         return func().upper()
#     return myinner
# @function
# def funname():
#     return "hllo"

# print(funname())

def fun(function):
    def myinner():
        return function().lower()
    return myinner

@fun
def funnmae():
    return "hello"

print(funnmae())



# def first_fun(name):
#     return name().upper()

# @first_fun
# def second_fun():
#     return "Name is raj"

# print(second_fun)

