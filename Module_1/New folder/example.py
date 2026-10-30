# mylist=[1,2,3,4,1,2,3,42,3,4,1]
# list=set(mylist)
# print(list)


name="Hello Good morning"

# print(name[::-1])
# for i in name.split():
# #     print(i,end=" ")
#     if i != "Good":
#         print(i, end=" ")
        

# def myfun(x):
#     return x[::-1]

# mytxt=myfun("hello")

# print(mytxt)




"Add sum "

# print()
# x=input("num")
# y=input("num")

# sum=int(x)+int(y)

# print(sum)



"make username "
"name :dax panchal"
"output :DL"

# fname=input("Enter the name : ")
# lname=input("Enter the lname :")
# print(fname,lname)

# username=fname[0].upper()+lname[6].upper()
# print(username)


"Voting age"

# name=input("Enter your name ")
# age=int(input("enter your age "))


# if age >=18:
#     print(f"{name} can vote")
# else:
#     print(f"{name}cant vote")


'''"Instructions
Read a score from input (0 to 100).

Print the letter grade:

90 or more: A
80 to 89: B
70 to 79: C
60 to 69: D
Below 60: F"'''

# score=int(input("enter "))

# if score >= 90:
#     print("A")
# elif score > 80:
#     print("B")
# elif score >70:
#     print("C")
# elif score >60:
#     print("D")
# else:
#     print("F") 

# n = int(input())
# for i in range(1, 11):
#     print(str(n) + " x " + str(i) + " = " + str(n * i))

"Multpications"

# n=int(input("Enter th number "))
# "5 X 1 =%"
# ans=n 

# for i in range(1,11):
#     print(str(n) +"X" + str(i)+"=" +str(n*i))


# "5 x 1 = 5"

# # n=int(input())

# # for i in range(1,11):
# #     print(str(n) +"X"+str (i)+ "=" + str(n*i)) 




"Sum of number"


n=int(input("enter the number: "))
total=0

for i in range(n):
    total += n

    print("Sum: " + str(total))

"Read the shape and find the measurements "


# import math

# shape=input().strip()

# if shape == "rectangle":
#     h=float(input())
#     w=float(input())
#     area=w*h
# elif shape == "triangle":
#     b=float(input())
#     h=float(input())
#     area=b*h/2    
# elif shape == "circle":
#     r=float(input())
#     area=math.pi*r*r
# print("Area: "+ format(area, ".2f"))    



# import math
# shape = input().strip().lower()
# if shape == "rectangle":
#     w = float(input())
#     h = float(input())
#     area = w * h
# elif shape == "triangle":
#     b = float(input())
#     h = float(input())
#     area = b * h / 2
# elif shape == "circle":
#     r = float(input())
#     area = math.pi * r * r
# else:
#     print("Invalid shape")
# print("Area: " + format(area, ".2f"))



import math

shape = input().strip().lower()

if shape == "rectangle":
    w = float(input())
    h = float(input())
    area = w * h

elif shape == "triangle":
    b = float(input())
    h = float(input())
    area = b * h / 2

elif shape == "circle":
    r = float(input())
    area = math.pi * r * r

else:
    print("Invalid shape")
    exit()

print("Area: " + format(area, ".2f"))
