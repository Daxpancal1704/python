# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n* fact(n-1)

# print(fact(4))    


def fact(n):
    if n == 0 :
        return 1
    else:
        return n*fact(n-1)
print(fact(10))


# def myfun(*args):
#     return sum (args)
# print(myfun(10,20,30))

# def myFun(**kwargs):
#     for k ,value in kwargs.items():
#         print(k,value)

# myFun(a=1,b=2,c=3) 




# s=[1,2,3,4,5]
# result=map(int,s)
# print(list(result))




a=[" Alice","Bob "]
ans=map(str.strip,a)

print(list(ans))