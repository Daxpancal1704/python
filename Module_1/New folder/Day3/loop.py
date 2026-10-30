# a=int(input("Enter the first number :"))
# b=int(input("Enter the second number :"))

# if a < b :
#     print("Biggr then a")
# else:
#     print("Smaller then a")


# if a > 0 or  b > 0:
#     print("a Number is postive")
# else:
#     print("Negetive Number")


"Using a variable"


# is_login=False

# if is_login:
#     print("Welcome")


"Using elif conditions"


# a=int(input("Enter the First Number :"))
# b=int(input("Enter the Second Number :"))


# if a > b:
#     print("B is bigest then a")
# elif a % 2 == 0:
#     print("a is even number")
# elif a== b :
#     print("a and b are equal")
# elif b % 2 ==0:
#     print("b is even number")


"Multiple elif statement"

# number = int(input("Enter the number: "))

# if number <= 0:
#     print("Enter a valid number")
# elif number <= 10:
#     print("10 number is big")
# elif number <= 30:
#     print("30 number is big")
# elif number < 100:
#     print("Valid number")
# else:
#     print("Number is big")



"Else as Fallback"

# name="dax"

# if len(name) > 0:
#     print(f"Welcome {name} ")
    
"Shorthand if"


# a=int(input("Enter the number : "))
# b=int(input("Entr the number : "))

# if a > b : print(" ")

# print("Numbr is even") if  a % 2 == 0  and b % 2 == 0 else print("Number is Odd")

# print("Number is postive ") if a > 0 else print("Numbr is negaitve")



list=[1,2,3,4,4,5]

for x in list:
    if x!= 4:
        print(x , end ="")
print()


"Multiple condition is one line"


a=10
b=21

print("even") if a %2 == 0 and b %2==0 else print("odd")
print("a and b are equal") if a ==b else print("Not equal") if a >b else print("a")


# a=10
# b=100


# max=a if a  > b else b
# print(max)



"Shorhand if elese with use of logical operator"


# num1=int(input("Enter the  first Number: "))
# num2=int(input("enter the  Sencond Number: "))
# num3=int(input("Enter the third number: "))


# if num1 > num2 and num2 > num3 :
#     print("All are true") 



"Nested if statement"


# x=41

# if x>10:
#     print("Above ten, ")
#     if x>20:
#         print("also above 20")
#     else:
#         print("but not above 20.")


# age=11
# has_approve=True
# hasnot_approve=False
# if age >= 18:
#     print("Approved")
#     if has_approve:
#         print("Going to the license")
#     elif hasnot_approve:
#         print("Under the age")
# else:
#     print("You are not eligable to get a license")



# name="Dax"
# age=23
# today_atten=True
# if name=="Dax":
#     if age == 22:
#         print("is valid")
#     elif today_atten:
#         print(f"yes he is present/but age is {age}")
#     else:
#         print("not present")
# else:
#     print("This name is invalid")



# name=input("Enter the correct name : ")
# age=int(input("Enter the correct age : "))
# present=True

# if name == "Dax" or name == "Raj":
#     print("name ia valid")
#     if age >=30:
#         print("age is valid")
#         if present:
#             print(f"Yes {name} is present ")
#         else:
#             print(f"{name} is a invalid name")
#     else:
#         print(f"{age} is invalid")
# else:
#     print("Enter the correct name")


# temp=input("Enter the Temperatur : ")
# is_sunny=True

# if temp >= "30c" and is_sunny:
#     print("That's cool") 
# else:
#     print("That's not cool")



"Login Form"


print("------------Login Form-------------")

# username=input("Enter the username : ")
# password=input("Enter the password : ")
# its_valid=True

# if username and password:
#     if username=="Dax" and password == "123321":
#         print("Username and password is valid")
#     else:
#         print("Both are not matching")
# else:
#     print("accepte only vali entry")
