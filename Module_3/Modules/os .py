#Import OS module
import os
import re

#os.path.basename() 'return the final components'
out = os.path.basename("C:/projects/report.txt")
print(out)



#os.path.dirname(path) return the diretory portion of a path
paths=r'C:\Users\dax.panchal\Desktop\Python\session_2.ipynb'
dirname=os.path.dirname(paths)
print(dirname)


# #os.path.isabs()  -> check wheather path is abously path
print(os.path.isabs(r'C:\Userss\dax.panchal\Desktop\Python\session_2.ipynb'))


#os.path.isdir() -> check wheather specified path exists and is  a directory (check the  dir)
print(os.path.isdir(r'C:\Users\dax.panchal\Desktop\Python'))

#os.path.isfile() -. check file is exists

print(os.path.isfile("session_3.ipynb"))


#os.path.normcase() -> check path is normalize
out = os.path.normcase("C:/Projects/Report.txt")
print(out)


#os.path.normpath() -> use for removing unnecessary speactors and refrences.
out = os.path.normpath("projects/./reports/../report.txt")
print(out)




path=r"C:\Users\dax.panchal\Desktop\Python\README.md"

if os.path.exists(path):
    print("yes")
else:
    print("NO")

print(os.path.getmtime(r"C:\Users\dax.panchal\Desktop\Python\README.md"))


















# import os 
# "show ing the curent working directory"
# cwd=os.getcwd()
# print("Current working diretectoy : ",cwd)

# print()
# def ospath(lable):
#     print(f"Current working directory : {lable}")
#     print(os.getcwd())

# ospath("before")
# print()
# os.chdir('../')  #remove dierectory
# ospath("after")
# print()

# dir="demo"
# parent_dir="C:/Users/dax.panchal/Desktop/Python/Module_3"
# path=os.path.join(parent_dir,dir)
# os.mkdir(path)
# print(os.getcwd())