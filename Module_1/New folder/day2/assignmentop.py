# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))

# print(a+b)
# print(a==b)#check the equality of two numbers
# a+=100#add 100 to the value of a
# print(a)    
# a^=100
# print(a)
# a>>=100
# print(a)
# print(x:=a+b)#walrus operator use to assign the value to the variable and return the value of the variable


'Ternary operator in python'


# num=int(input("Enter the number:"))

# x="Even" if num%2==0 else "Odd"
# print(x)

# y="Good" if  num == 10 else num == 12 if num == 14 else "Bad"
# print(y)


"Comparison operator in python"

# num1=int(input("Enter the first number:"))
# num2=int(input("Enter the second number:"))     

# print(num1 == num2)#check the equality of two numbers
# print(num1 != num2)#check the inequality of two numbers
# print(num1 > num2)#check the greater than of two numbers
# print(num1 < num2)#check the less than of two numbers
# print(num1 >= num2)#check the greater than or equal to of two numbers
# print(num1 <= num2)#check the less than or equal to of two numbers


"Logical operator in python"

# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))

# print(a<=10 and b<=10)

# print(a>b or a<b)

# print(not(a and b))


"Identity Opertor"


# list=[1,2,3,4,5]
# list1=[1,2,3,8,4,5]
# list2=list=list1
# print(list2)
# print(list2 is  list1 )
# print(list is list1)
# print(list == list1)

"Memebership operator"

# list=["a","b","c"]
# print("a" in list or "b" not in list)

"Bitwise operator"

a=int(input("Enter the first numbr :"))
b=int(input("Enter the Seocd number :"))

print(a & b)#and operator# suppose a=10 so 10=1010 and b=12so 12=1100  ans is 1010+1100=1000

print(a|b) #or operator if any 1 or 1 so 1
print(a^b)#XOR operator 
print(~b)#invert all bits it means suppose b is 12 and 12 binary number is 1100 so add 1 so look like this 1100+1=1101 1101 is a 13 and invert means -13
print(a<<b)#left shft operator 
print(a>>b)