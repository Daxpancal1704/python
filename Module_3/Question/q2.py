"""### Question 2 (Easy) - Class variable, classmethod and staticmethod
Create a class `Student` with `name` and `marks`.
* A **class variable** `count` that increases by 1 every time a student object is created.
* A **class method** `get_count()` that returns `count`.
* A **static method** `is_pass(marks)` that returns `True` when marks are **50 or more**.

```python
s1 = Student("Asha", 82)
s2 = Student("Ravi", 45)
s3 = Student("Meera", 91)
print(Student.get_count())
print(Student.is_pass(s1.marks), Student.is_pass(s2.marks))
```
```
3
True False
```"""





class Student:

    count=0

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        Student.count +=1

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def is_pass(marks):
        return marks >= 50

s1=Student("ALice",89)
s2=Student("Lice",90)
s3=Student("Jice",20)
print(Student.get_count())
print(Student.is_pass(s1.marks),Student.is_pass(s2.marks),Student.is_pass(s3.marks))


        