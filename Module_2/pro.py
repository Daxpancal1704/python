
"""import json
import os
from pathlib import Path
import math

# ---------------- CONFIGURATION ----------------

MAX_EMPLOYEES = 5

# Dynamic folder path
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

MAIN_FILE = DATA_DIR / "employees.json"


# ---------------- FILE HANDLING ----------------

def get_files():
    files = sorted(
        DATA_DIR.glob("employees*.json"),
        key=lambda p: 1 if p.name == "employees.json"
        else int(p.stem.split("_")[1])
    )
    return files


def load_file(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            raise ValueError(f"{file.name} must contain a list")

        for emp in data:
            if not isinstance(emp, dict):
                raise ValueError("Invalid employee record")
            if not all(k in emp for k in
                       ("id", "name", "department", "salary", "active")):
                raise ValueError("Employee record has missing fields")
            if (type(emp["id"]) is not int or
                    not isinstance(emp["name"], str) or
                    not isinstance(emp["department"], str) or
                    type(emp["salary"]) not in (int, float) or
                    not math.isfinite(emp["salary"]) or
                    type(emp["active"]) is not bool):
                raise ValueError("Invalid employee field types")

        return data

    except json.JSONDecodeError as e:
        raise ValueError(f"Corrupted JSON: {file.name}") from e


def save_file(file, employees):
    temp = file.with_name(file.name + ".tmp")

    try:
        with open(temp, "w", encoding="utf-8") as f:
            json.dump(employees, f, indent=4)
        os.replace(temp, file)

    finally:
        if temp.exists():
            temp.unlink()


def initialize():
    if not MAIN_FILE.exists():
        save_file(MAIN_FILE, [])


def load_all():
    files = get_files()

    if not files or MAIN_FILE not in files:
        raise ValueError("Main employee file is missing")

    records = []

    for file in files:
        records.extend((file, emp) for emp in load_file(file))

    ids = [emp["id"] for _, emp in records]

    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate IDs found in storage")

    return records


# ---------------- EMPLOYEE OPERATIONS ----------------

def add_employee():
    try:
        records = load_all()

        emp_id = int(input("Enter employee ID: "))

        if any(emp["id"] == emp_id for _, emp in records):
            print("Error: Duplicate employee ID")
            return

        name = input("Enter name: ").strip()
        department = input("Enter department: ").strip()
        salary = float(input("Enter salary: "))

        if not name or not department:
            print("Name and department cannot be empty")
            return

        if not math.isfinite(salary) or salary < 0:
            print("Invalid salary")
            return

        employee = {
            "id": emp_id,
            "name": name,
            "department": department,
            "salary": salary,
            "active": True
        }

        files = get_files()
        target = files[-1]

        employees = load_file(target)

        if len(employees) >= MAX_EMPLOYEES:
            # Create the next numbered file
            if target.name == "employees.json":
                next_num = 2
            else:
                next_num = int(target.stem.split("_")[1]) + 1

            target = DATA_DIR / f"employees_{next_num}.json"
            employees = []

            if target.exists():
                employees = load_file(target)
                if len(employees) >= MAX_EMPLOYEES:
                    print("Storage file is unexpectedly full")
                    return

        employees.append(employee)
        save_file(target, employees)

        print("Employee added successfully!")

    except ValueError as e:
        print("Input/Storage error:", e)
    except OSError as e:
        print("File permission or file error:", e)


def remove_employee():
    try:
        records = load_all()
        emp_id = int(input("Enter employee ID to remove: "))

        for file, emp in records:
            if emp["id"] == emp_id:
                employees = load_file(file)
                employees = [
                    e for e in employees if e["id"] != emp_id
                ]
                save_file(file, employees)
                print("Employee removed successfully!")
                return

        print("Employee ID not found")

    except ValueError as e:
        print("Error:", e)
    except OSError as e:
        print("File error:", e)


def update_salary():
    try:
        records = load_all()
        emp_id = int(input("Enter employee ID: "))

        for file, emp in records:
            if emp["id"] == emp_id:
                salary = float(input("Enter new salary: "))

                if not math.isfinite(salary) or salary < 0:
                    print("Invalid salary")
                    return

                employees = load_file(file)

                for e in employees:
                    if e["id"] == emp_id:
                        e["salary"] = salary
                        break

                save_file(file, employees)
                print("Salary updated!")
                return

        print("Employee ID not found")

    except ValueError as e:
        print("Error:", e)
    except OSError as e:
        print("File error:", e)


# ---------------- COMPREHENSIONS ----------------

def view_active():
    records = load_all()
    employees = [emp for _, emp in records]

    # List comprehension
    active_employees = [e for e in employees if e["active"]]

    for emp in active_employees:
        print(emp)


def department_summary():
    records = load_all()
    employees = [emp for _, emp in records]

    department = input("Enter department (blank for all): ").strip()

    # Names in a given department
    dept_names = [
        e["name"] for e in employees
        if e["department"].lower() == department.lower()
    ]

    # Salary greater than a threshold
    try:
        threshold = float(input("Salary threshold: "))
        if not math.isfinite(threshold):
            print("Invalid threshold")
            return
    except ValueError:
        print("Invalid threshold")
        return

    high_salary = [
        e for e in employees if e["salary"] > threshold
    ]

    # Dict comprehension
    dept_counts = {
        dept: sum(1 for e in employees if e["department"] == dept)
        for dept in {e["department"] for e in employees}
    }

    # Set comprehension
    unique_departments = {
        e["department"] for e in employees
    }

    print("\nDepartment names:", dept_names)
    print("Employees above threshold:", high_salary)
    print("Department counts:", dept_counts)
    print("Unique departments:", unique_departments)


# ---------------- GENERATOR & REPORT ----------------

def report_lines(employees):
    # Generator: yields one formatted line at a time
    for emp in employees:
        status = "Active" if emp["active"] else "Inactive"
        yield (
            f'{emp["id"]} | {emp["name"]:<8} | '
            f'{emp["department"]:<6} | '
            f'{emp["salary"]:>8.2f} | {status}'
        )


def generate_report():
    try:
        records = load_all()
        employees = [emp for _, emp in records]

        report_file = DATA_DIR / "report.txt"

        with open(report_file, "w", encoding="utf-8") as f:
            f.write("ID | Name     | Dept   | Salary   | Status\n")
            f.write("-" * 52 + "\n")

            for line in report_lines(employees):
                f.write(line + "\n")

        print("Report generated:", report_file)

    except (ValueError, OSError) as e:
        print("Report error:", e)


# ---------------- MENU ----------------

def main():
    try:
        initialize()

        while True:
            print("\n===== EMPLOYEE MANAGEMENT =====")
            print("1. Add employee")
            print("2. Remove employee")
            print("3. Update salary")
            print("4. View active employees")
            print("5. View department summary")
            print("6. Generate report (txt)")
            print("7. Exit")

            choice = input("Enter choice: ").strip()

            try:
                if choice == "1":
                    add_employee()
                elif choice == "2":
                    remove_employee()
                elif choice == "3":
                    update_salary()
                elif choice == "4":
                    view_active()
                elif choice == "5":
                    department_summary()
                elif choice == "6":
                    generate_report()
                elif choice == "7":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid menu choice")

            except (ValueError, OSError) as e:
                print("Operation failed:", e)

    except (ValueError, OSError) as e:
        print("Application could not start:", e)


if __name__ == "__main__":
    main()

"""
"""
from collections import Counter
import json
from pathlib import Path
import re

# 0. Define file paths using pathlib
BASE_DIR = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
NOTES_FILE = BASE_DIR / "notes.txt"
STATS_FILE = BASE_DIR / "notes_stats.json"

# 1. Collect user input and append to notes.txt
print("Enter your notes (type 'quit' to finish):")
with open(NOTES_FILE, mode="a", encoding="utf-8") as f:
    while True:
        user_input = input("> ")
        if user_input.strip().lower() == "quit":
            break
        f.write(user_input + "\n")

# Initialize tracking variables for statistics
total_lines = 0
total_words = 0
longest_line = ""
word_counter = Counter()

print("\n--- Current Notes ---")

# 2. Read the file by looping over the file object
with open(NOTES_FILE, mode="r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, start=1):
        # Print every line with its line number
        print(f"{line_num}: {line.endwith('\n') and line or line + '\n'}", end="")
        
        # Strip newline for accurate length and statistics processing
        clean_line = line.rstrip("\n")
        
        # Track statistics
        total_lines += 1
        
        if len(clean_line) > len(longest_line):
            longest_line = clean_line
            
        # Clean words (removing punctuation, case-insensitive)
        words = re.findall(r"\b\w+\b", clean_line.lower())
        total_words += len(words)
        word_counter.update(words)

# Extract the 3 most frequent words
most_common_words = [word for word, count in word_counter.most_common(3)]

# 3. Print the computed statistics
print("\n--- Statistics ---")
print(f"Total number of lines: {total_lines}")
print(f"Total number of words: {total_words}")
print(f"Longest line: '{longest_line}'")
print(f"3 most frequent words: {', '.join(most_common_words)}")

# 4. Save statistics into notes_stats.json
stats_data = {
    "total_lines": total_lines,
    "total_words": total_words,
    "longest_line": longest_line,
    "most_frequent_words": most_common_words
}

with open(STATS_FILE, mode="w", encoding="utf-8") as json_file:
    json.dump(stats_data, json_file, indent=4, ensure_ascii=False)

print(f"\nStatistics successfully saved to {STATS_FILE.name}")
"""

"""
from pathlib import Path

# Define the custom exception for unknown operators
class UnsupportedOperatorError(Exception):
    #Raised when the user provides an operator not in the supported list.
    pass

def safe_calculator():
    # Define file paths safely using Path.cwd() (Jupyter/Notebook safe)
    BASE_DIR = Path.cwd()
    HISTORY_FILE = BASE_DIR / "history.txt"
    
    supported_operators = {'+', '-', '*', '/', '//', '%', '**'}
    history = []
    attempt = 0

    print("=== Safe Command-Line Calculator ===")
    print("Format: 'number operator number' (e.g., 12 / 4, 2 ** 10)")
    print("Type 'q' to quit at any time.\n")

    while True:
        try:
            # Capture Ctrl+C inside the loop nicely
            user_input = input("Enter expression: ").strip()
            
            if user_input.lower() == 'q':
                print("\nExiting calculator...")
                break
                
            if not user_input:
                continue

            attempt += 1
            
            # 1. Handle format validation
            parts = user_input.split()
            if len(parts) != 3:
                raise ValueError("Format must be exactly three parts: 'number operator number'.")
            
            raw_num1, operator, raw_num2 = parts

            # 2. Handle unknown operator validation
            if operator not in supported_operators:
                raise UnsupportedOperatorError(f"Operator '{operator}' is not supported.")

            # 3. Handle non-numeric operand validation
            # Convert to float (or int if it's a whole number)
            num1 = float(raw_num1)
            num2 = float(raw_num2)
            if num1.is_integer(): num1 = int(num1)
            if num2.is_integer(): num2 = int(num2)

            # TRY BLOCK: Perform the core calculation
            if operator == '+': result = num1 + num2
            elif operator == '-': result = num1 - num2
            elif operator == '*': result = num1 * num2
            elif operator == '/': result = num1 / num2
            elif operator == '//': result = num1 // num2
            elif operator == '%': result = num1 % num2
            elif operator == '**': result = num1 ** num2

        except ValueError as e:
            # Catches both string formatting splits and float conversion errors
            if "could not convert string to float" in str(e):
                print("Error: Operands must be valid numbers.")
            else:
                print(f"Error: {e}")
                
        except UnsupportedOperatorError as e:
            print(f"Error: {e}")
            
        except ZeroDivisionError:
            print("Error: Division or modulo by zero is not allowed.")
            
        except KeyboardInterrupt:
            # Handles Ctrl+C safely during typing
            print("\n[Ctrl+C detected] Exiting calculator cleanly...")
            break
            
        else:
            # ELSE BLOCK: Executes only if calculations succeed
            output_str = f"{num1} {operator} {num2} = {result}"
            print(f"Result: {output_str}")
            history.append(f"{user_input} -> {output_str}")
            
        finally:
            # FINALLY BLOCK: Always runs after an evaluation attempt
            if 'user_input' in locals() and user_input.lower() != 'q':
                print(f"--- attempt #{attempt} done ---\n")

    # Save tracking history to history.txt upon exiting cleanly
    if history:
        try:
            # Open without reading using mode 'a' (append data so old history isn't erased)
            file_obj = open(HISTORY_FILE, "a", encoding="utf-8")
            for record in history:
                file_obj.write(record + "\n")
            file_obj.close()
            print(f"Session history successfully saved to: {HISTORY_FILE}")
        except Exception as e:
            print(f"Failed to write history file: {e}")

if __name__ == "__main__":
    # Wrap the root call to catch Ctrl+C if hit exactly at startup prompt
    try:
        safe_calculator()
    except KeyboardInterrupt:
        print("\nCalculator terminated before initialization.")
"""































import json
import os
from pathlib import Path

# -----------------------------
# SETTINGS
# -----------------------------

FOLDER = Path(__file__).parent
MAX_EMPLOYEES = 5

FIRST_FILE = FOLDER / "employees.json"


# -----------------------------
# FILE FUNCTIONS
# -----------------------------

def get_files():
    """Find all employee JSON files."""

    files = []

    for file in FOLDER.glob("employees*.json"):
        if file.name == "employees.json":
            files.append((1, file))

        elif file.stem.startswith("employees_"):
            number = file.stem.replace("employees_", "")

            if number.isdigit() and int(number) >= 2:
                files.append((int(number), file))

    files.sort(key=lambda x: x[0])
    return files


def create_file():
    """Create the first file if missing."""

    if not FIRST_FILE.exists():
        with open(FIRST_FILE, "w") as f:
            json.dump([], f)


def read_file(file):
    """Read employee records from JSON."""

    try:
        with open(file, "r") as f:
            data = json.load(f)

        if not isinstance(data, list):
            raise ValueError("JSON must contain a list")

        for emp in data:
            if not isinstance(emp, dict):
                raise ValueError("Invalid employee record")

        if len(data) > MAX_EMPLOYEES:
            raise ValueError("File exceeds employee limit")

        return data

    except json.JSONDecodeError:
        raise ValueError(f"Corrupted JSON file: {file.name}")


def save_file(file, employees):
    """Save employee records."""

    with open(file, "w") as f:
        json.dump(employees, f, indent=4)


def load_all():
    """Read employees from all files."""

    create_file()

    all_employees = []
    locations = {}

    for number, file in get_files():
        employees = read_file(file)

        for emp in employees:
            emp_id = emp["id"]

            if emp_id in locations:
                raise ValueError("Duplicate employee ID in files")

            locations[emp_id] = file
            all_employees.append(emp)

    return all_employees, locations


# -----------------------------
# ADD EMPLOYEE
# -----------------------------

def add_employee():
    try:
        employees, locations = load_all()

        emp_id = int(input("Enter employee ID: "))

        if emp_id in locations:
            print("Employee ID already exists!")
            return

        name = input("Enter name: ").strip()
        department = input("Enter department: ").strip()

        if not name or not department:
            print("Name and department cannot be empty!")
            return

        salary = float(input("Enter salary: "))

        if not os.path.isfinite(salary) or salary < 0:
            print("Enter a valid non-negative salary!")
            return

        active = input("Is employee active? (yes/no): ").lower()

        if active not in ("yes", "no"):
            print("Enter yes or no!")
            return

        new_employee = {
            "id": emp_id,
            "name": name,
            "department": department,
            "salary": salary,
            "active": active == "yes"
        }

        # Find a file with space
        target = None

        for number, file in get_files():
            data = read_file(file)

            if len(data) < MAX_EMPLOYEES:
                target = file
                break

        # If all files are full, create a new file
        if target is None:
            files = get_files()
            next_number = max(n for n, f in files) + 1
            target = FOLDER / f"employees_{next_number}.json"
            save_file(target, [])

        data = read_file(target)
        data.append(new_employee)
        save_file(target, data)

        print("Employee added successfully!")

    except (ValueError, OSError) as e:
        print("Error:", e)


# -----------------------------
# REMOVE EMPLOYEE
# -----------------------------

def remove_employee():
    try:
        employees, locations = load_all()
        emp_id = int(input("Enter employee ID to remove: "))

        if emp_id not in locations:
            print("Employee not found!")
            return

        file = locations[emp_id]
        data = read_file(file)

        data = [emp for emp in data if emp["id"] != emp_id]

        save_file(file, data)
        print("Employee removed successfully!")

    except (ValueError, OSError) as e:
        print("Error:", e)


# -----------------------------
# UPDATE SALARY
# -----------------------------

def update_salary():
    try:
        employees, locations = load_all()
        emp_id = int(input("Enter employee ID: "))

        if emp_id not in locations:
            print("Employee not found!")
            return

        salary = float(input("Enter new salary: "))

        if not os.path.isfinite(salary) or salary < 0:
            print("Enter a valid non-negative salary!")
            return

        file = locations[emp_id]
        data = read_file(file)

        for emp in data:
            if emp["id"] == emp_id:
                emp["salary"] = salary
                break

        save_file(file, data)
        print("Salary updated successfully!")

    except (ValueError, OSError) as e:
        print("Error:", e)


# -----------------------------
# VIEW ACTIVE EMPLOYEES
# -----------------------------

def view_active():
    try:
        employees, locations = load_all()

        # List comprehension
        active_employees = [
            emp for emp in employees if emp["active"]
        ]

        if not active_employees:
            print("No active employees.")
            return

        for emp in active_employees:
            print(emp)

    except (ValueError, OSError) as e:
        print("Error:", e)


# -----------------------------
# DEPARTMENT SUMMARY
# -----------------------------

def department_summary():   
    try:
        employees, locations = load_all()

        # Dictionary comprehension
        departments = {
            dept: sum(1 for emp in employees
                      if emp["department"] == dept)
            for dept in {emp["department"] for emp in employees}
        }

        # Set comprehension
        unique_departments = {
            emp["department"] for emp in employees
        }

        print("\nDepartment counts:", departments)
        print("Unique departments:", unique_departments)

        # Names in a given department
        dept = input("Enter department to search: ").strip()

        names = [
            emp["name"] for emp in employees
            if emp["department"].lower() == dept.lower()
        ]

        print("Employees in department:", names)

        # Employees earning above a threshold
        try:
            threshold = float(input("Enter salary threshold: "))

            if not os.path.isfinite(threshold):
                print("Invalid threshold!")
                return

            high_salary = [
                emp for emp in employees
                if emp["salary"] > threshold
            ]

            print("Employees earning above threshold:")
            for emp in high_salary:
                print(emp)

        except ValueError:
            print("Invalid salary threshold!")

    except (ValueError, OSError) as e:
        print("Error:", e)


# -----------------------------
# REPORT GENERATOR
# -----------------------------

def generate_lines(employees):
    """Generator: produce one report line at a time."""

    for emp in employees:
        status = "Active" if emp["active"] else "Inactive"

        yield (
            f"{emp['id']} | "
            f"{emp['name']:<10} | "
            f"{emp['department']:<10} | "
            f"{emp['salary']:>10,.2f} | "
            f"{status}"
        )


def generate_report():
    try:
        employees, locations = load_all()

        report_file = FOLDER / "report.txt"

        with open(report_file, "w", encoding="utf-8") as f:
            f.write("ID | Name | Department | Salary | Status\n")
            f.write("-" * 65 + "\n")

            for line in generate_lines(employees):
                f.write(line + "\n")

        print("Report created:", report_file.name)

    except (ValueError, OSError) as e:
        print("Error:", e)


# -----------------------------
# MAIN MENU
# -----------------------------

def main():
    while True:
        print("\n--- EMPLOYEE MANAGEMENT ---")
        print("1. Add employee")
        print("2. Remove employee")
        print("3. Update salary")
        print("4. View active employees")
        print("5. View department summary")
        print("6. Generate report (txt)")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            remove_employee()

        elif choice == "3":
            update_salary()

        elif choice == "4":
            view_active()

        elif choice == "5":
            department_summary()

        elif choice == "6":
            generate_report()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
