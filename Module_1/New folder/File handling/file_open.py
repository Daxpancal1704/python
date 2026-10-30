"File handling used to open file , (x)created file ,(r)read file , (w)Write file ,if file is not exits and so use the (a)append so file is created and writing start  "
"'t' use the default tet mode  "
"'b' use the open in binary mode "


"only open file and showing"

# file=open(r"C:\Users\dax.panchal\Desktop\Python\File handling\class.txt","r")
# data=file.readlines()
# print(data)


"Create a file and writing "

# file=open(r"C:\Users\dax.panchal\Desktop\Python\File handling\demo","w")

# # file.write("Hello Good morning\n")
# # file.write("Hello Good morning\n")
# # file.write("Hello Good morning\n")


# print(file)



"append a content without deleting original content"


# file=open(r"C:\Users\dax.panchal\Desktop\Python\File handling\demo","a")

# file.write("Good ")
# print(file)



"x creating a new file file name is alreay exists then  show me FileExists Error "


# file=open(r"C:\Users\dax.panchal\Desktop\Python\File handling\demo","x")
# file.write("HelloGod ")
# print(file)




" use of  'with open()'  file "


# with open(r"C:\Users\dax.panchal\Desktop\Python\File handling\demo","r") as file :
#     data=file.read()
#     print(data)

# with open(r"C:\Users\dax.panchal\Desktop\Python\File handling\demo","a") as file1:
#     data1="\ngood morning1"
#     file1.write(data1)
#     data1=file1.write("\nGood Morning")
#     print(data1)    


"with accessing the loop"


# with open(r"C:\Users\dax.panchal\Desktop\Python\File handling\demo","r")as file:
    # for line in file:
    #     print(line.upper().strip())
    #     print(line.title())
        # print(file.read(3))
        # print(file.tell())
        # print(file.seek())


"if checking any file exists ye or no use the from pathlib import Path "

# from pathlib import Path

# data= Path(r"C:\Users\dax.panchal\Desktop\Python\File handling\demo")


# if data.exists():
#         print("yes")
# else:
#         print("No")       



"Use the try except to handling the error "


# try:
#     with open(r"C:\Users\dax.panchal\Desktop\Python\File handling\demo")as file:
#         print(file.read())
# except FileNotFoundError:
#     print("Not found")



"Student data Management"
"example: Name:Dax,marks:100"


with open(r"File handling\demo","w")as file:
    file.write("Dax,23,Ai/Ml\n")
    file.write("Rax,22,Python\n")


with open(r"File handling\demo","r")as file:
    for line in file:
        name ,age,Department=line.strip().split(",")
        print(f"Hello my name is {name},my age is {age}, and i'm working in {Department}")
        print(file.readline())
        print(file.readlines())
file.close()

import os
"Remove the file"
os.remove(r"File handling\class.txt")
"remove the folder"

# os.rmdir("")


"def __eq__(self,other):"
"           return self.name=other.name and self.age=other.age"












# with open(r"C:\Users\dax.panchal\Desktop\Python\File handling\student","w")as file:
#     file.write("Dax,100\n")
#     file.write("ram,20\n")
#     file.write("syam,10\n")
#     print(file)


# with open(r"C:\Users\dax.panchal\Desktop\Python\File handling\student","r")as file:

#    for i in file:
#     name,marks=i.strip().upper().split(",")
#     print(f"name{name},marks{marks}")    