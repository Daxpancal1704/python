"Match statement"

a=10
match a:
    case 1:
        print("Monday")
    case 2:
        print("Tus") 
    case 3:
        print("wed")
    case _:
        print("no")


"Combine value"

day=12

match day:
    case 1|2|3|4|5:
        print("same")
    case 6|7|8|9|10|11|12|13:
        print("good")


"Using if condition"

name =2
match name:
    case 1 if name == 13:
        print("ok") 
    case 2 : 
        print("not")   