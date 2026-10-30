# """try:
#     num=int(input("Number :"))
#     print(num)

# except ValueError as e:
#     print("error : ",e)

# finally:
#     print("ok done")    """



# """defining the custom exceptions"""
# """
# class InvalidAgeException(Exception):
#     "Raised when the input value is less then 18"
#     pass

# num=18
# try:
#     input_num=int(input("Number: "))
#     if num >input_num:
#         raise InvalidAgeException
#     else:
#         print("Eligible to vote")
# except InvalidAgeException:
#     print("Exrption")"""



# class SalaryNotInRangeError(Exception):
#     """Exception rais for erroes in inout salary
#     Attributes:
#         salary : input salary which caused the error
#         message: exaplasion of thr error
#     """
#     def __init__(self,salary,message):
#         self.salary=salary
#         self.message=message
#         super().__init__(self.message)
# salary=int(input("salary: ")) 
# if not 5000 < salary < 10000:
#             raise SalaryNotInRangeError(salary)

"""
Given a string, return a string where for every char in the original, there are two chars.


double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'"""     

def double_char(str):
    result=''
    for i in str:
        result += i*2
    return result

print(double_char("Hello"))




# def double_char(string):
#     result = ""
#     for char in string:
#         result += char * 2
#     return result


# def count_code(s):
#     count = 0
#     for i in range(len(s) - 3):
#         if s[i : i + 2] == "co" and s[i + 3] == "e":
#             count += 1
#     return count
"""def end_other(a, b):
    # Convert both strings to lowercase to ensure case-insensitivity
    a_lower = a.lower()
    b_lower = b.lower()
    
    # Check if either string ends with the other
    return a_lower.endswith(b_lower) or b_lower.endswith(a_lower)"""


"""a=abcxyz
   b=abxyz
   
   end =xyx  true"""

# a="abcxyz"
# b="abxyz"

def end_other(a, b):
  a=a.lower()
  b=b.lower()


  return  (b.endswith(a) or a.endswith(b))
print(end_other('HiAbc', 'abc'))