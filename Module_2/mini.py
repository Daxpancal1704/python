import json
import os
import math
from pathlib import Path


BASE_URL=Path(__file__).parent
FILE_NAME=BASE_URL / "demo.json"
MAX_EMP=5

def get_file():
    "Search file for globly"

    files=[]

    for file in BASE_URL.glob("demo.json"):
        if file.name == "demo.json":
            files.append((1,file))
        elif file.stem.startswith("demo_"):
            number=file.stem.replace("demo", "")

            if number.isdigit() and int(number) >2:
                files.append((int(number),file))

    files=sorted(key=lambda x : x[0])
    return files        

def create_file():
    if not FILE_NAME.exists():
        with open(FILE_NAME,"w")as f:
            json.dump([],f)

def read_file(file):

    try:
        with open(file,"r")as read:
            data=json.load(read)

            if  not isinstance(data ,list):
                raise ValueError()

            for emp in data:
                if not isinstance(emp,dict):
                    raise ValueError()

            if len(data) > MAX_EMP:
                raise ValueError()
            return data

    except json.JSONDecodeError:
       raise ValueError()

def save_file(file,employees):
    with open(file,"w")as write:
        json.dump(employees,write,indent=4)

def load_all():

    create_file()
    all_employees=[]
    location={}

    for number,file in get_file():
        employee=read_file(file)



        for emp in employee:
            emp_id=emp['id']

            if emp_id in location:
                raise ValueError("emp id duplicate")

            location[emp_id]=file
            all_employees.append(emp)

    return all_employees,location

def add_employees():
    try:
        employees,location=load_all()

        emp_id=int(input("Enter emp id: "))
        
        if emp_id in location:
            print("emp already exit")
            return

        name=input("emp name : ")
        department=input("emp department : ")

        if not name or not department:
            print("emp name and department can't empty")
            return
        salary=float(input("Enter salary : "))
        if not math.isfinite(salary) or salary  < 0:
            print("eter a valid salary")

        active=input("emp active yes or no ").strip().lower()

        if active not in ("yes","no"):
            print("enter yes or no")
            return

        emp_data={
            "id":emp_id,
            "name":name,
            "department":department,
            "salary":salary,
            "active":active == "yes"
        } 
        target=None

        for number,file in get_file():
            data=read_file(file)


            if len(data) < MAX_EMP:
                target = file
                break

        if target == None:
            files=get_file()
            next_number=max(n for n,f in files) +1
            target=BASE_URL / f"demo({next_number}.json"
            save_file(target,[])

        data=read_file(target)
        data.append(emp_data)
        save_file(target,data)

    except (ValueError,OSError)as e:
        print(e)


def remove_emp():
    try:
        employees,locations=load_all()

        emp_id=int(input("Enter remove id : "))
        if emp_id not in locations:
            print("emp id not found")
            return

        file=locations[emp_id]
        data=read_file(file)


        data=[emp for emp in data if emp['id'] != emp_id]

        save_file(data,file)

    except (ValueError,OSError)as e:
        print(e)

def update_salary():
    try:
        employees,locations=load_all()
        emp_id=int(input('Enter emp id :'))
        if emp_id not in locations:
            print("emp id not found ")
            return
        salary=float(input("Enter your new salary : "))
        if not os.path.isfinite(salary) or salary < 0:
            print("enter a valid not-negative salary")
            return


        file=locations[emp_id]
        data=read_file(file)
        for emp in data:
            if emp['id']==emp_id:
                emp['salary']==salary
                break
        save_file(file, data)
        print("successfully salsary updated")
    except (OSError,ValueError)as e:
        print(e)

def view_employee():
    try:
        employess,locations=load_all()

        actv_emp=[emp for emp in employess if emp['active']] 
        if not actv_emp:
            print("emp are not active")
            return

        for emp in actv_emp:
            print(emp)
    except (OSError,ValueError) as e:
        print(e)

def view_department():
    try:
        employees ,locations=load_all()
        department={
            dept:sum(1 for emp in employees
            if emp['department'] == dept)
            for dept in {emp['department'] for emp in employees}
        }
        unique_department={emp['department'] for emp in employees}

        print(f"\n Department count:{department}")
        print(f"Unique_department : {unique_department}")

        dept=input("Enter department name : ").strip()

        names=[emp['name'] for emp in employees if emp['department'].lower()==dept.lower()]

        print("Employees in department",names)
        
        try:
            threshold=float(input("Enter a salary threshold ."))

            if not os.path.isfinite(threshold):
                print("Invalid Threshold")
                return

            high_salary=[emp for emp in employees if emp['salary'] > threshold]
            print("Employees earning abouve salary ")
            for emp in high_salary:
                print(emp)

        except ValueError:
            print("INnvalide threshold.")
             

    except (OSError,ValueError)as e:
        print(e)

def genrated_lines(employees):

        for emp in employees:
            status="active" if emp['acitve'] else 'deactive'

            yield{
                f"{emp['id']} |"
                f"{emp['name'] :<10} |"
                f"{emp['department'] :<10} |"
                f"{emp['salary'] :>10,.2f} |"
                f"{status}"
            }

def generated_reports():
    try:
        employees,locations=load_all()

        report_file=BASE_URL / "demo.txt"

        with open (report_file , mode="w",encoding='utf-8')as f:
            f.write("ID | NAME | DEPARTMENT | SALARY | STATUS \n")
            f.write("-" * 65+ "\n")            
            