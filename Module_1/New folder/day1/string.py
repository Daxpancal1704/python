# this is a multiline string formate


name="""Dax Panchal
hello , my name is dax pancahal and i am a python developer
i have 2 years of experience in python and i have worked on many projects"""
print(name)

name1='''Dax Panchal
hello , my name is dax pancahal and i am a python developer
i have 2 years of experience in python and i have worked on many projects'''
print(name1) 



# a="Hello, my self dax panchal"

# print(a[0])

# # for i in "Dax Panchal":
# #     print(i)


# print(len(a))

# myintro="Hello, Good Morning! , my self  Dax panchal and i'm python dec=veloper and cuurely i'm fresher in Kody technlolabs"
# print(len(myintro))
# if "Hellos" not in myintro:
#     print("yes, it is good")
# else:
#     print("no, it is not good")    



#Slicing method 

# name="Dax,Panchal"

# print(name[2:])

"Modify String"

# print(name.upper())
# print(name.lower())
# print(name.strip())# use the removing the white space from the string
# print(name.replace("Dax","lax"))# replace() method use to replace the any character and string
# print(name.split(","))# split() method use to split the string into list





"concatenations in string"

# name="Dax"
# name1="panchal"
# age=str(23)

# ans=name+" "+name1+" "+age
# print(ans)


"f-string formate and placeholder"

# name="Dax"
# age=23
# salary=100000
# ans=f"Hello Good Moring my name {name} is and my age is {age} years old and my salary is {salary:.3f} per month"
# print(ans)

"Escape sequence in string"

# # name="dax panchal is a \"python\" developer"
# name1="Dax 1panchal \000 dax"
# # print(name)
# print(name1)

"capitalize() method in string "
# name="dax panchal is a good men"
# print(name.capitalize())#first character is a uppercase and all other character is lowercase
"casefold() method in string"
# name1="dax panchal Is a good men"
# print(name1.casefold())#every character is a lowercase
"center() method in string"
# name2="dax panchal"
# print(name2.center(50, ","))
"count() method in string"
# name3="He panchal is a good men and He panchal is a good men"
# print(name3.count("a",0,100))#count("a",start,end) method use to count the character in string

# name="Dax panchal"
# # print(name.endswith("panchal", 4,11))
# print(name.endswith(("panchal", "Dax")))#endwith() method use to check the string is end with the given character or not


# name="Dax panchal"
# print(name.title())#title() method use to convert the first character of each word is a uppercase and all other character is lowercase  

# name1="Dax panchal"
# print(name1.find("l", 0, 11))#find() method use to find the character in string and return the index of character if not found then return -1


name2="my name is dax panchal and ,my {salary:.2f} per month".format(salary=100000)#format() method use to format the string and replace the placeholder with the given value
# print(name2.format(salary=10))#format() method use to format the string and replace the placeholder with the given value
print(name2)