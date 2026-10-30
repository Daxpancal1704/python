import json
from pathlib import Path
import os 
import math

# # // File path 

FOLDER=Path(__file__).parent
MAX_EMP=5
FILE_NAME=FOLDER / "employee.json"


# '''// file Handling //'''


def get_file():
    """Finde all emplyees json file """

    files=[]

    for file in FOLDER.glob("employee*.json"):
        if file.name=="employee.json":
            files.append((1,file))

        elif file.stem.startswith("employee_"):
            number=file.stem.replace("employee_","")

            if number.isdigit() and int(number) >= 2:
                files.append((int(number),file))
    files.sort(key=lambda x :x[0])
    return files


def create_file():
    """create the first file if missing"""

    if not FILE_NAME.exists():
        with open(FILE_NAME,"w")as f:
            json.dump([],f)


def read_file(file):
    """read the employee reocord"""

    try:
        with open(file,"r") as f:
            data=json.load(f)

            if not isinstance(data, list):
                    raise ValueError("JSON must contain a list")
            
            for emp in data:
                if not isinstance(emp, dict):
                    raise ValueError("Invalid employee record")
            
            if len(data) > MAX_EMP:
                raise ValueError("File exceeds employee limit")            
            return data
            
    except json.JSONDecodeError:
        raise ValueError(f"Corrupted JSON file: {file.name}")

def save_file(file, employee):
    """Save employee records."""

    with open(file, "w") as f:
        json.dump(employee, f, indent=4)

def load_all():
    """Read employee from all files."""
    
    create_file()
    
    all_employee = []
    locations = {}

    for number, file in get_file():
        employee = read_file(file)

        for emp in employee:
            emp_id = emp["id"]

            if emp_id in locations:
                raise ValueError("Duplicate employee ID in files")

            locations[emp_id] = file
            all_employee.append(emp)

    return all_employee, locations

def add_employee():
    try:
        employees , locations = load_all()

        emp_id=int(input("enter id : "))

        if emp_id in locations:
            print("Emp id already exits")
            return
        name=input("Enter Name : ").strip().lower()
        department=input("Enter departmnt : ").strip().lower()

        if not name or not department :
            print("name and emp_department can't be empty")
            return
        
        salary=float(input("Enter salary :  "))
        if not math.isfinite(salary) or salary < 0:
            print("enter a valid non-negative salary")
            return

        acitve=input("Is employee activa (yes/no)").strip().lower()


        if acitve not in ('yes','no'):
            print("Enter in yes or no")
            return

        new_emp = {
    "id": emp_id,
    "name": name,
    "department": department,
    "salary": salary,
    "active": acitve == "yes"
}
         # Find a file with space
        target = None
        
        for number, file in get_file():
            data = read_file(file)
            
        
            if len(data) < MAX_EMP:
                target = file
                break
            
                # If all files are full, create a new file
        if target is None:
            files = get_file()
            next_number = max(n for n, f in files) + 1
            target = FOLDER / f"employee_{next_number}.json"
            save_file(target, [])
        
        data = read_file(target)
        data.append(new_emp)
        save_file(target, data)
        
        print("Employee added successfully!")
        
    except (ValueError, OSError) as e:
                print("Error:", e)
    






def remove_employee():
    try:
        employee,locations=load_all()

        emp_id=int(input("Enter remove emp id : "))
        if emp_id not in locations:
            print("Emp id not found")
            return

        file=locations[emp_id]
        data=read_file(file)

        data=[emp for emp in data if emp["id"]!=emp_id]

        save_file(file,data)
        print("employeee remove successfully ")
    except (ValueError,OSError) as e:
        print(e)



def update_salary():
    try:
        employee,locations=load_all()

        emp_id=int(input("enter employee id : "))
        if emp_id not in locations:
            print("employee not found")
            return

        salary=float(input('enter New salary : '))
        if not os.path.isfinite(salary) or salary< 0:
            print("emter a valid not - negative salary ")
            return

        file=locations[emp_id]
        data=read_file(file)

        for emp in data:
            if emp['id']==emp_id:
                emp["salary"] = salary
                break
        save_file(file,data)
        print("successfuly salary uodated")
        
    except (ValueError,OSError)as e:
        print(e)

def view_employee():
    try:
        employee,locations =load_all()
        active_emp=[
            
            emp for emp in employee if emp['active']
        ]
        if not active_emp:
            print("employees are not active")
            return

        for emp in active_emp:
            print(emp)

    except (ValueError,OSError)as e:
        print(e)

def view_depart():
   try:
               employee, locations = load_all()
       
               # Dictionary comprehension
               departments = {
                   dept: sum(1 for emp in employee
                             if emp["department"] == dept)
                   for dept in {emp["department"] for emp in employee}
               }
       
               # Set comprehension
               unique_departments = {
                   emp["department"] for emp in employee
               }
       
               print("\nDepartment counts:", departments)
               print("Unique departments:", unique_departments)
       
               # Names in a given department
               dept = input("Enter department to search: ").strip()
       
               names = [
                   emp["name"] for emp in employee
                   if emp["department"].lower() == dept.lower()
               ]
       
               print("Employee in department:", names)
       
               # Employee earning above a threshold
               try:
                   threshold = float(input("Enter salary threshold: "))
       
                   if not os.path.isfinite(threshold):
                       print("Invalid threshold!")
                       return
       
                   high_salary = [
                       emp for emp in employee
                       if emp["salary"] > threshold
                   ]
       
                   print("Employee earning above threshold:")
                   for emp in high_salary:
                       print(emp)
       
               except ValueError:
                   print("Invalid salary threshold!")
       
   except (ValueError, OSError) as e:
        print("Error:", e)
      
def genrate_lines(employee):
   for emp in employee:
       status="active" if emp["active"] else "Inactive"


       yield(
           f"{emp['id']} | "
           f"{emp['name']:<10} | "
           f"{emp['department']:<10} | "
           f"{emp['salary']:>10,.2f} | "
           f"{status}"
       )

def genrate_report():
    try:
        employee ,locations=load_all()


        report_file=FOLDER /"report.txt"

        with open(report_file ,mode="w",encoding='utf-8')as f:
            f.write("ID | Name | Department | Salary | Status\n")
            f.write("-" * 65 + "\n")

            for line in genrate_lines(employee):
                f.write(line +"\n")

            print("Report created:", report_file.name)

    except (ValueError, OSError) as e:
        print("Error:", e)



def main():
    while True:
        print("____Employee Management___ ")
        print("1. Add employee")
        print("2. Remove employee")
        print("3. Update Salary")
        print("4. View active employee")
        print("5. View department summary")
        print("6. Generate report (txt)")
        print("7. Exit")


        choice=input("Enter choice ...")

        if choice =="1":
            add_employee()
        elif choice =="2":
            remove_employee()
        elif choice =="3":
            update_salary()
        elif choice == "4":
            view_employee()
        elif choice == "5":
            view_depart()
        elif choice == "6":
            genrate_report()
        elif choice == "7":
            print("Exit")
            break
        else:
            print("Envalid choice try aging !")

if __name__ == "__main__":
    main()
