"""1. Temperature converter
Parameters and return

Easy

Write celsius_to_fahrenheit(c) that converts Celsius to Fahrenheit.celsius_to_fahrenheit(0) → 32.0"""

# def celsius_to_fahrenheit(c):
    
#     fahrenheit=c * 9 / 5 + 32
#     print(fahrenheit)

# c=float(input('enter c : '))
# celsius_to_fahrenheit(c)
"""
2. Password validator
Conditions and Boolean return

Easy

Write is_valid_password(password). Return True if the password has at least 8 characters; otherwise return False.is_valid_password('python123') → True"""



# def is_valid_password(password):

#     speical_ch="!@#$^&*"

#     if len(password) >=8 and any(char not in speical_ch for char in password):
#        return True
#     else:
#         return False

# password=input("enter the passowrd: ")
# print(is_valid_password(password))

"""[ ] 
3. Shopping bill
Default arguments

Easy

Write calculate_bill(price, quantity, discount=0). Calculate the total after applying the discount percentage.calculate_bill(100, 2, 10) → 180.0

Hide hint
Get a hint
Hint: Subtotal is price × quantity. Subtract discount/100 of the subtotal."""

# def calculate_bill(price,quntity,dicount=0):

#         price=price*quntity
#         dicount=price*dicount/100
#         total=price-dicount
#         print("total : ",total)


# price=float(input("Price : "))
# quantity=int(input("Quantity: "))
# dicount=float(input("dicount(%): "))
# calculate_bill(price,quantity,dicount)
    

"""[x] 
4. Flexible total
*args

Easy

Write total_cost(*prices) that returns the sum of any number of prices.total_cost(100, 250, 50) → 400""" 



# def total_cost(*price):
#         return sum(price)

# price=input("price ")
# price=[int(prices) for prices in price.split(",")]
# print(total_cost(*price))
        

"""[x] 
5. User profile
**kwargs

Easy

Write display_profile(**details) that prints each key and value on a separate line.display_profile(name='Sam', city='Mumbai')

Hide hint
Get a hint
Hint: Loop through details.items()."""


# def display_profile(**details):

#     for key,value in details.items():
#         print(key,value)
# display_profile(name="sam",city="Mumbai")


"""[ ] 
6. Flexible calculator
Functions as arguments

Medium

Write calculate(a, b, operation) where operation is a function passed into calculate. Use it to perform addition and multiplication.calculate(4, 5, add) → 9

Hide hint
Get a hint
Hint: Call operation(a, b) inside calculate. Pass add, not add()."""

# def add(a,b):
#     return a+b

# def mul(a,b):
#     return a*b

# def calculator(a,b,operation):
#     return operation(a,b)

# print(calculator(10,20,add))
# print(calculator(10,20,mul))


"""7. Employee salary
Keyword and default arguments

Medium

Write calculate_salary(basic, bonus=0, tax_rate=10). Return the salary after adding the bonus and deducting tax.calculate_salary(30000, bonus=5000) → 31500.0

Hide hint
Get a hint
Hint: Tax is a percentage of basic + bonus. Return the amount after deducting it."""


# def calculate_salary(basic, bouns=0,tax_rate=10):

#     gross_salary=basic + bouns
#     tax_amout=gross_salary * tax_rate/100
#     final=gross_salary-tax_amout
#     return final
# print(calculate_salary(30000,5000))

"""[ ] 
8. Discount creator
Closures

Medium

Write make_discount(percent) that returns a function. The returned function accepts a price and applies the discount.ten_off = make_discount(10); ten_off(200) → 180.0"""


def make_discount(precent):
    def dicount(price):
        dicount_amo=price*precent/100
        return  price- dicount_amo

    return dicount



ten_off = make_discount(10)
print(ten_off(200))
