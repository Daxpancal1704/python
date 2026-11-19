"python applies an internal  optimization callled object interning for small immutable object.insted of creating a new object every time ,python reuses same object to save memory.   "

x=10
y=20

if id(x) == id(y):
    print("x and y are same")
else:
    print(f"x {id(x)} and y {id(y)}  are not same obejct")