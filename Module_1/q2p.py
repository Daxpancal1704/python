"""Question 2. Marks Processor

Write a program that takes all of its input from the user through prompts. First, ask the
user how many students there are. Then, for each student, ask separately for the name and
the score.

The program must keep asking again, with an error message, if the user enters:
a. A number of students that is not a positive whole number
b. A score that is not a whole number between 0 and 100

Write a function grade(score) that returns:
● A for 90 and above
● B for 75 to 89
● C for 60 to 74
● D for 40 to 59
● F below 40

Store each student as a tuple (name, score) in a list. After all the input is collected, print:
1. Each student’s grade in the order they were entered, as name: grade
2. The class average rounded to 2 decimal places, as Average: x
3. The topper(s), sorted alphabetically and comma-separated, as Topper(s): name1,
name2
4. The number of students in each grade that appears, ordered from A to F, as Grade
count: A=2, B=1"""


# Write function to grade(score) and find some socre and return

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


#get student a number
while True:
    try:
        n=int(input("Enter a number:"))
        if n > 0:
            break
        print("Error: Enter a positive whole  number ")
    except ValueError:
        print("Error: Enter a positive whole number ")

for i in range(n):
    name=input("Enter student name : ")

    while True:
       try:
            score=int(input("Enter student score :"))
            if 0 <= score <= 100:
                break
            print("Error : Score must be between 0 to 100")
       except ValueError:
           print("Enter a whole number")
    student.append((name,score))

#print student's grade 
# 
for name ,score in student:
    print(name+ ":" +grade(score))  

#Calculate average

total=0

for name ,score in student:
    total+=score

average=total/len(student)
print(f"average : {average:.2f}")


#finde topper

highest=max(score for name ,score in student)

topprer=[]
for name ,score in student:
    if score == highest:
        topprer.append(name)
topprer.sort()
print("topper(s)" + "," .join(topprer) )        


#count grade


count={}
for name ,score in student:
    g=grade(score)
    count[g]=count.get(g,0)+1

result=[]
for g in ["A","B","C","D","F"] :
    if g in count:
        result.append(g + "=" + str(count[g]))

print("Grade count: " + ", ".join(result))


