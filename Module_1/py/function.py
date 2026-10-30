"""def factorials(x):
    if x == 1:
        return 1
    else:
        return(x*factorials(x-1))
factorials(3)


def rescursion(number):
    if number == 0:
        print("Done")
    else:
        print(number)
        rescursion(number-1)

rescursion(10)

"""
def fibonacci(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))



"""if __name__ == '__main__':
    students = []

    for _ in range(int(input("Enter your valid num :"))):
        name = input("name : ")
        score = float(input("score : "))
        students.append([name, score])

    scores = sorted(set([student[1] for student in students]))
    second_lowest = scores[1]

    names = [student[0] for student in students if student[1] == second_lowest]

    names.sort()

    for name in names:
        print(name)

    print(students)    """

# if __name__ == '__main__':
#     stu=[]
#     for  _ in range(int(input())):
#         name=input("name :")
#         score=float(input("score :"))
#         stu.append([name,score])

#     socors=sorted(set([stus[0] for stus in stu]))
#     second_low=score[1]

#     names=[stus[0] for stus in stu if stu[1]==second_low]

#     names.sort()

#     for name in names:
#         print(name)

#     print(stu)      