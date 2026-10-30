# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": [1964,1956,2002]
# }
# print(thisdict)
# print(thisdict["brand"])
# print(len(thisdict))


# thisdict1=dict(name="ram",age=23)
# print(type(thisdict1))


"usethe .get() methd to access the any value in variable"

# x=thisdict1.get("name")
# print(x)

".key() use the find the key in dictioaries"

# x1=thisdict1.keys()
# print(x1)


"Add new item "
# thisdict1["colour"]="dark"
# print(thisdict1)


# x2=thisdict1.values()
# print(x2)


# thisdict1["age"]=21
# print(thisdict1)



"Find the all item usethis method item()"


# x4=thisdict1.items()
# print(x4)



# if "model" in thisdict1:
#     print("Yes ,it's present")
# else:
#     print("Not present")


"Update the key and value using the update() method"

# print(thisdict1)

# thisdict1.update({"name":"dax"})
# print(thisdict1)


# print()

# "pop()remove the specific key"
# print(thisdict1)


# thisdict1.pop("colour")
# thisdict1.popitem()
# print()
# print(thisdict1)


"del useing the delte the key and pair"


# del thisdict1["name"]
# print(thisdict1)



# thisdict1.clear()
# print(thisdict1)


student = {
    "name": "Dax",
    "age": 20,
    "marks": 85.5,
    "passed": True,
    "skills": ["Python", "Django", "ML"],
    "languages": ("English", "Hindi"),
}


print(student)
for x,y in student.items():
    print(x,y )


stu_detils={
    "child1":{
        "name":"Dax",
    },
    "child2":{
        "name":"ram",
    },
}
print(stu_detils)

print(stu_detils["child1"]["name"])