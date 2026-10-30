"List item also ordered and changeble and allow the dublicate value and start with index [0]"

# fruits=["apple","banana","cherry"]
# print(len(fruits))
# print(fruits)
# print(len(fruits))
# print(fruits[-1])
# print(fruits[-2:-1])

# if "mango" in fruits:
#     print("yes")
# else:
#     print("no")


# fruits[1:2]="blackcurrant","mango"
# print(fruits)

"use insert value to specific position"

# fruits.insert(4,"Rose")
# print(fruits)

"useing append method to add any items to end of the list"


# fruits.append(4)
# print(fruits)


"extend list us the append list to another list"

# veges=["Potato",
# "Tomato",
# "Carrot",
# "Onion"]
# name=("ram","shyam")

# fruits.extend(name)
# print("this is ",fruits)
# fruits.extend(veges)
# print(fruits)
# print(fruits[6])



# name=list(("ram"))
# print(type(name))
# ans=fruits[0]  "find the value in list"
# ans=fruits.append["chiku"]
# print(ans)


"Removeing specified item"




# print(fruits)
# print(name)
# print(veges)
# fruits.append("cherry")
# print(fruits)
# fruits.remove("cherry")
# print(fruits)
# fruits.pop(1)#pop() metho use the remove the last item and also removing  the specified items
# print(fruits)
# fruits.pop(0)
# # del fruits[0]
# print(fruits)

# veges.clear()#use the clear the whle list it means list is empty
# print(veges)



"loop in list"

list_loop=["AUDI","BMW","Hyundai","Range Rover"]
# for i in list_loop:
#     print(i)


# for X in range(len(list_loop)):
#     print(list_loop[X],end=" ")


i=0

while i < len(list_loop):
    print(list_loop[i])
    i=i+1


# fruits = ["apple", "banana", "cherry", "kiwi", "apple","mango"] 
# # ans=[x for x in fruits if "apple" in x ]
# # ans.remove("apple")
# # print(ans)


# range_ex=[x for x in range(100) if x % 2==0 and x < 50 ]
# print(range_ex)

# remove_apple=[x for x in fruits if x != "apple"]
# print(remove_apple)



# new_fruits=[]



# for x in fruits:
#     if "a" or "o" or "e" in x:
#         new_fruits.append(x)

# print(new_fruits)        



# i=0

# while i < len(new_fruits):
#     print(new_fruits )
#     i=i+1

"Sort in list"

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

# for x in thislist:
#     if x != "orange":
#         print(x , end=",")
# print()
# thislist.append("watermelon")
# print(thislist)

# for y in thislist:
#     if y != "mango" and y!="kiwi":
#         print(y)



"Number sorting"

# number=[6,1,2,3,4,5,1,2,0]
# number.sort()# this is asending order
# print(number)

# print()

# number.sort(reverse=True)
# print(number)

# new_number=set(number)
# print(new_number)


# thislist = ["Orange", "mango", "kiwi", "Pineapple", "banana"]

# thislist.sort(reverse=True)
# print(thislist)



# "Copy list"


# name=["name","age"]
# age=[12,34,55,56]

# name.extend(age)
# print(name)
# name2=list(name[0:1])
# name1=name.copy()
# print(name1)
# print(name2)



name="Hello How are you?"
result=""
for char in name:
    if char in "aeiou":
        result=result+char
print( result)        