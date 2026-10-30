" all method with example "

# list=["name","age","number"]

"append method"

# list.append("Gender")
# print(list)

"clear Method use the clear the all value in list/array etc"

# list.clear()
# print(list)

"Copy method"

# list1=list.copy()
# print(list1)

"count() method to count the special string or any number in list /array "
# list1=[1,1,1,1,2,2,2,33,3,3]
# a=list1.count(1)
# print(a)

"extend() method use the merage rhe two colum and of the list"
# list.extend(list1)
# print(list)

"index() rturn the index of the first element"

# print(list.index("name"))

"insert() add element to specific position"


# list.insert(5,"lname")
# list.insert(1,"lname")
# print(list)

"pop() remove the element specific position"

# list.pop(1)
# print(list)

"remove() remove the any  item when you write in () "

# print(list.remove("age"))
# print(list)

"reverse() the sorting element"

# list.reverse()
# print(list)

"sort() use the sorting method"
# print(list)
# list.sort()
# print(list)




"----------------Dictionary Methods--------------"

dict={
    "name":"dax",
    "age":23,
    "number":9345645678
}

# print(dict)



"clear()  use the clear means empty dictionary"
# dict.clear()
# print(dict)

"copy() ue the copy dictionary"

# dict1=dict.copy()
# print(dict1)

"fromkeys()  retrun dict to specified key and value"

# x=("dax","ram")
# y=(1,2,3,4)

# thi=dict.fromkeys(x,y)
# print(thi)


"get() return value from specifed value"

# print(dict)

# x=dict.get("name")
# y=dict.get("age")
# print(x,y)

# dict.items()
# print(dict)
# a=dict.keys()

# print(a)



a=dict.values()
print(a)

dict.update({"name":"Dax"})
print(dict)

dict.popitem()
print(dict)