"""A single python file conating a module"""
"# from mymodule <- ' mymoduel is a file name it means my own module'"
"# import greet  <- it menas import the greet functionin mymodule"
from mymodule import greet,sum,add
from math import *
import math as m
print(sqrt(36))
print(factorial(10))

print(greet("dax"))
print(sum(10,20))
print(add(10,20))


"Built-in module "

import platform

# x=platform.system
# y=dir(platform)

# print(x)
# print(y)

print(m.pi)


import requests

r=requests.get("https://www.geeksforgeeks.org/python/python-modules/")
print(r.status_code)
import sys

print(dir(sys))



