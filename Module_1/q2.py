def grade(score):
    if score >=90:
        return "A"
    elif score >=75:
        return "B"
    elif score >=60:
        return "C"
    elif score >=40:
        return "D"
    else:
        return "F"

student=[]


while True:
    try:
        n=int(input("Enter a number: "))
        if n >0:
            break
        print("Error : Enter a whole number")
    except ValueError:
        print("Error : Enter a whole number")

for i in range(n):
    name=input("Enter a name : ")
    while True:
        try:
            score=int(input("Enter a score: "))
            if 0 <= score <= 100:
                break
            print("Enter score must be between 0 to 100")
        except ValueError:
            print("Enter a whole number")
    student.append((name,score))

for name ,score in student:
    print(name+":",grade(score))            

#print the average

total=0
for name ,score in student: 
    total+=score
average=total/len(student)
print(f"Average is :{average:.2f}")      

#Find the topper

highest=max(score for name,score in student )

topper=[]

for name ,score in student:
    if score == highest:
        topper.append(name)
topper.sort()
print("topper(s):"+",".join(topper))


count={}

for nam,score in student:
    g=grade(score)
    count[g]=count.get(g,0)+1

result=[]

for g in ["A","B","C","D","F"]:
    if g in count:
        result.append(g + "=" + str(count[g]))
print("Grade count: " + ", ".join(result))
