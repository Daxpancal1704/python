"""### Question 3 (Easy-Medium) - Using the standard library
a) **`math`** - read a number `n` and print its square root, its factorial (if `n` is a whole number from 0 to 10) and `gcd(n, 12)`. For `n = 6`: `2.449489742783178`, `720`, `6`.

b) **`datetime`** - read two dates in the format `DD-MM-YYYY`. Print the number of days between them and the ISO weekday number (Monday = 1) of the first date.
```
17-08-2026
20-08-2026
```
```
Days between: 3
Weekday number: 1
```
c) **`random`** - from the list `["Asha", "Ravi", "Meera", "Kabir"]` pick one winner with `random.choice()` and print `Winner: <name>`. (The name changes on every run.)"""



# import math

# n=int(input("Enter a number: "))
#  #a) read a number n and print its square root 

# print("Square root of n :",  math.sqrt(n))

# if 0 <= n <= 100:
#     print("Factorial of n :",math.factorial(n))
# else:
#     print("Factorial is not allowed ")

# print("Gcd is :",math.gcd(n,12))



#b) datetime modules 

from datetime import datetime

#Read two Dates
 
# date1=input("Enter first Date format(DD-MM-YYYY):")
# date2=input("Enter Second Date format(DD-MM-YYYY):")


# # Converting str in to datetime foramte
# d1=datetime.strptime(date1,"%d-%m-%Y")
# d2=datetime.strptime(date2,"%d-%m-%Y")

# print("Date1 is : ",d1)
# print("Date2 is : ",d2)

# #differ
# diff=abs((d2-d1).days)
# print("Days betwwen: ",diff)
# print("Weekday number : ",d2.isoweekday())



#c) random from th list chosse to one random member


import random

names=["Asha","Ravi","Meera","Kabir"]

winner=random.choice(names)
print("winner : ",winner)