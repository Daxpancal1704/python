x="dax"

def myfunc():
    global x
    x= "panchal"
    print("this is my function", x)
myfunc()

print("this is my global variable", x)