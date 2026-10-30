# def string():
#     """Hello good Morning"""
#     print("my self ")
# string()
# str=string.__doc__
# print(str)



"Types hints -Describe the what type of data type expeted"


# def add(a:int,b)->int:
#     return a + b

# print(add(10,10))

"Passing fun as a arguments"


# def add(n):
#     return n*n

# def sum(add,value):
#     return add(value)

# print(sum(add,10))


"Closure function"

# def multi(factors):
#     def mul(number):
#         return number * factors

#     return mul

# a=multi(2)
# b=multi(3)
# print(a(10),b(10))











"Closure function it means one function and inside another function first function parameter call in inside functin so that is called cloure functions"




# def fun1(values):
#     def fun2(values1):
#         return values**values1
#     return fun2


# a1=fun1(10)
# a2=fun1(20)
# print(a1(10))
# print(a2(20))



"Decorators it means Add a behavior to a function"
"it means function to add a behaviour without changing the original function code "
"Decorators comanly  use for logging, timing ,authorization checks and caching"

"it is simpl example with no argument"
# def decorators(func):
#     def wrapper():
#         print("Before the calling decorators")
#         func()
#         print("After calling dcorators")
#     return wrapper

# @decorators

# def greet():
#     print("Decoroatr calling ")
# greet()



# def function1(fun):
#     def inner():
#         print("hello")
#         fun()

#     return inner 
# @function1
# def greet():
#     print("hello1")
# greet()  

"A resuable decorators usally uses *args and **kwargs"

from functools import wraps

# def my_dector(func):
#     @wraps(func)
#     def wrapper(*args,**kewgrs):
#         print("calling Functions")
#         return func(*args,**kewgrs)
#     return wrapper    
# @my_dector
# def gret(a,b):
#     """Hello Good Morning.."""
#     print("helo")
#     return a+b-a
# print(gret.__doc__)
# print(gret(10,100))

def my_dector(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("calling arg")
        return func(*args,**kwargs)

    return wrapper
@my_dector
def greet(a,b):
    return a + b

print(greet(10,20))


"""wreapper function wrap the anther function and add the functionlty before or after execution"""
"""
def wrapper(func):
    def inner():
        print("Hello this is inner()")
        func()
        print("After wrapper() function call")
    return inner

def greet():
    print("hello")
greet=wrapper(greet)
greet()"""


# def wrapper(fun):
#     def inside():
#         print("hello inside")
#         fun()
#         print("hello inside")

#     return inside

# @wrapper

# def greet():
#     print("good")
# greet()




"Generators it is a special type of function that produce once at a time "


# def num():
#     yield 1
#     yield 2
#     yield 3

# result=num()    
# print(next(result))
# print(next(result))
# print(next(result))


# def square(n):
#     for i in range(1,n+1):
#         yield i*i

# res=square(5)

# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))



# def cal(func ,n):
#     return func(n)


# print(cal(lambda x:x+4,6))




# import time

# def timer(func):
#     def inner(*args,**kwrgs):
#         start=time.time()
#         result=func(*args,**kwrgs)
#         end=time.time()
#         print("Execution time: ",round(end-start,6),"second")
#         return result
#     return inner

# @timer
# def calculate():
#     tottal=0
#     for i in range(10000):
#         tottal+=i
# calculate()        





# def a_decorator(func):
#     def wrapper(*args, **kwargs):
#         """A wrapper function"""
#         # Extend some capabilities of func
#         func()
#     return wrapper

# @a_decorator
# def first_function():
#     """This is docstring for first function"""
#     print("first function")

# @a_decorator
# def second_function(a):
#     """This is docstring for second function"""
#     print("second function")

# print(first_function.__name__)
# print(first_function.__doc__)
# print(second_function.__name__)
# print(second_function.__doc__)



def decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        """A wrapper function"""
        func()
    return wrapper


@decorator
def f_fun():
    """This is decorator first function"""
    print("first function")

@decorator
def s_fun():
    """This is Second function"""
    print("secodn function")    

print(f_fun.__name__)
print(s_fun.__name__)
print(f_fun.__doc__)
print(s_fun.__doc__)



