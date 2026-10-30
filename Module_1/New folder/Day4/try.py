# try:

#     list=["name","age","gender"]

#     for i in list:
#         if i != "name":
#                   print(i,list1)
            
#     print("Hello")
# except NameError:
#     print("Variabel not Defining")
# else:
#     print("exit")





"raise it is use the single line error handling"

age = 15

if age < 18:
    raise Exception("You must be 18 or older")

print("You can enter")