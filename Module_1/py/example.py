"Function with parameter"


# def greek(name):
#     print("Hello ",name)
# greek("Alice")


"function that retrun keyword"
"retrun keyword send a result back to the code back called th function "

# def add(a,b):
#     return a+b


# sum=add(10,20)
# print(sum)


"Default parameter"

# def default(name="Alice"):
#     print("hello,", name)

# default()



"function with multiple parameter"

# def  calu(a,b):
#     c=a+b
#     return c

# sum1=calu(100,20)
# print(sum1)



"Differenc print vs return"


# def first():
#     print(10)
# def second():
#     return 100

# x=first()    
# y=second()


# print("x=",x)
# print("y=",y)



"function inside another functions"

# def sequare(n):
#     return n * n

# def calulater(n):
#     return sequare(n) + 10

# print(calulater(10))



# def mul(n):
#     return n ** n

# def div(n):
#     return mul(n) /10

# print(div(10))



"Local variables"
# def var():
#     name="Aice"
#     age=23

#     print(f"Hello my name is {name} and my age is {age}")

# var()

"Positional argument"
"value are assigned to parameter based on their position"


# def intro(name,age):
#     print("My name is ",name)
#     print("my age is ",age)

# intro("Alice",23)


"Keywords argument"

"in keyword argument define spefic name n calling functions "


# def key_argu(name,age):
#     print(name,age)
#     return name ,age

# print(key_argu(name="elice",age=23))



" *argu acceepted multiple positional argument"


# def all_arg(*num):
#     print(sum(num))

# all_arg(10,20,30,30)

" **keyword accept the multiple keyword argument"


# def keyword_arg(**details):
#     return details

# ans=keyword_arg(name="Alice",age=23,number=12233)
# print(ans)

"Global variable"

# x=100
# def g_vaiable():
#     x=200
#     print(x)

# g_vaiable()

# print(x)

"global keyword"

# x=100
# def g_keyword():

#     global x
#     x=200
#     print(x)

# g_keyword()
# print(x)


"Recursion fuction call it self"


# def countdown(n):
#     if n == 0:
#         print("Done")
#     else:
#         print(n)
#         countdown(n-1)

# countdown(30)

"Factorial"


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n-1)

# print(factorial(4))



def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n-1)
print(fact(10))    
"Recursion"


# def countdo1(n):
#     if n == 0:
#         print("done")
#     else:
#         print(n)
#         countdo1(n-1)

# countdo1(10)


"lambda function it is a small anonymous functions"

"It is small functions"
# def sequare(n):
#     return n ** n

# print(sequare(10))

"with lambda function"


#Syntax
"lambda parameter: expression"
# seq=lambda n: n>8
# print(seq(5))


# even=lambda a:"even" if a % 2==0 else "odd" 
# print(even(10))





"Calulator with multiple function"


# try:
#     a=int(input("enter first number: "))
#     b=int(input("enter second number: "))
#     def add (a,b):
#         return a + b

#     def mul(a,b):
#         return a-b

#     def div(a,b):
#         return a/b

#     def sub(a,b):
#         return a*b

#     print(add(a,b))
#     print(mul(a,b))
#     print(div(a,b))
#     print(sub(a,b))
# except ValueError as e:
#     print("enter only number",e)


"Check Even or odd numberand if enter the string so genrate the error "


# try:
#     num=int(input("Enter thre number : "))
#     if num % 2 == 0:
#         print(f"{num} is even ")
#     else:
#         print(f"{num} is odd")

# except ValueError as e:
#     print("error: ",e)


"find the largest number of three but zero is not acceptabl "    

# def largest(a,b,c):
#         if a ==0 or b ==0 or c ==0:
#             print("Zero not alow")
#         elif a > b and a > c:
#             print(f"{a} is Bigger ")
#         elif b > a and b >c :
#             print(f"{b} is Bigger")
#         else:
#             print(f"{c} is Bigger")
    
# try:
#     a=int(input("first: "))
#     b=int(input("second: "))
#     c=int(input("third: "))
#     largest(a,b,c)
# except ValueError :
#     print("erorr:")


"Calculat the student grade"


# def student_marks(marks):

#     if marks == 0 :
#         print("Not allowed")
#     elif marks >80 and  marks <100:
#         print("A grade")
#     elif marks > 60 and marks<80 :
#         print("B grade")
#     elif marks > 50 and marks < 60:
#         print("C grade")
#     elif marks > 100:
#         print("Invalid")
#     else:
#         print("faile")

# try :
#     marks=int(input("Enter the number: "))

#     student_marks(marks)
# except ValueError as e:
#     print("error",e)

""""
Challenge 1 — Positive, negative, or zero
Write check_sign(n) so it returns "Positive", "Negative", or "Zero"."""


# def check_sign(n):
#     if n > 0:
#         return "positive"
#     elif n == 0:
#         return "zero"
#     else :
#         return "Negative"

# print(check_sign(10))    

"""
Challenge 2 — Sum from 1 to n
Write sum_numbers(n) that returns the sum of all integers from 1 through n. For example, sum_numbers(5) should return 15"""

# def sum_number(n):
#     total=0
#     for i in range(1,n+1):
#         total=total+i

#     print(total)
# sum_number(10)    
def sumnum(n):
    total=0
    for i in range(1,n+1):
        total+=i
    print(total)   
sumnum(10)
# def sum_number(n):
#     total=0
#     for i in range(1,n+1):
#         total += i
#     return total
# print(sum_number(5))

"""
Challenge 3 — Count vowels
Write count_vowels(text) that returns the number of vowels (a, e, i, o, u) in a string. For example, count_vowels("hello") should return 2."""

# def count_vowels(text):
#     count=0

#     for char in text.lower():
#         if char in "aeiou":
#             count=count+1
#     return count
# print(count_vowels("Name"))    











# def vowels(text):
#     count=0

#     for char in text.lower():
#         if char in "aeiou":
#             count=count+1

#     return count

# print(vowels("Dax panchal"))     


"Recursion"

# def resursion(n):
#     if n ==0:
#         print("Done !")
#     else:
#         print(n)
#         resursion(n-1)

# resursion(10)







"fctorial"


# def fact(n):
#     if n ==0 or n ==1:
#         return 1
#     return n * fact(n-1)

# print(fact(10))




"sum of number"

# def sumof(n):
#     store=0
#     for i in range(1,n+1):
#         store=store+i
#     print(store)
# sumof(5)        


"vowls"



# def vo(text):
#     co=0
#     for char in text.lower().upper():
#         if char in "aeiouAEIOU":
#             co=co+1
#     return co

# print(vo("DAI Panchal"))        






"Removing exta space"



# name="   'Python is fun'   "
# print(name.strip())

"""4. Count a character
Write a function that counts how many times "a" appears in "banana".
Expected output: 3
Hint: count()"""


# count_ch="banana"

# print(count_ch.count("a"))


"""5. Reverse a string
Write a function reverse_string(text) that returns the string reversed.
Example: reverse_string("Python") → "nohtyP"
Hint: Try slicing with a negative step."""


# def  reverse_string(text):


#     print(text[::-1])

# reverse_string(text="python")


"""6. Check for a palindrome
Write a function that checks whether a word reads the same forward and backward.
Example: is_palindrome("madam") → True
Example: is_palindrome("hello") → False"""


def is_palindrome(name):

    if name[::-1] == name:
        return True
    else :
        return False

print(is_palindrome("121"))


def pal(num):

    o_number=str(num)
    rever_num=o_number[::-1]

    if o_number == rever_num:
       print("true")
    else:
        print("false")
pal(121)       

""". Replace a word
Replace "bad" with "good" in "Python is bad".
Expected output: "Python is good"
Hint: replace()"""



# name="python is bad"

# print(name.replace("bad","good"))

"""
8. Count words
Write a function count_words(sentence) that returns the number of words in a sentence.
Example: count_words("Python is easy to learn") → 5
Hint: split() converts the sentence into a list of words."""


def count_words(sentence):
    # sentence="Python is easy to learn"
    print(sentence.split())

count_words(sentence="Python is easy to learn")


"""9. Normalize a username
Write a function that removes surrounding spaces and converts a username to lowercase.
Example: normalize("  PyThOn_Dev  ") → "python_dev"""



# def normalize():

#     name="  PyThOn_Dev  "
#     print(name.strip().lower())


# normalize()


"""10. Find the longest word
Write a function longest_word(sentence) that returns the longest word.
Example: longest_word("I love programming") → "programming"""



# def longest_word(sentence):

#     words=sentence.split()
#     return max(words,key=len)

# print(longest_word("I love programming"))


"""11. Count each word
Given "python is fun and python is powerful", count how many times each word appears.
Expected result:
{
    "python": 2,
    "is": 2,
    "fun": 1,
    "and": 1,
    "powerful": 1
}"""
text = "python is fun and python is powerful"

# Split the sentence into words and count their occurrences
word_counts = {word: text.split().count(word)  for word in text.split()}

print(word_counts)



"""12. Check an anagram
Write a function that checks whether two strings contain the same letters in a different order.
Example: is_anagram("listen", "silent") → True
Hint: Consider lower(), replace(), and sorted()."""


def is_anagram(word1,word2):

    word1=word1.lower()
    word2=word2.lower()

    return sorted(word1)==sorted(word2)


print(is_anagram("listen","slient"))



"""13. Sum all numbers
Write a function that returns the sum of all numbers in a list.
Example: sum_list([10, 20, 30, 40]) → 100
Hint: sum()"""


# list=[10,20,30,40]

# asn=sum(list)
# print(asn)


"""14. Find the largest number
Find the largest element without using max().
Example: [12, 45, 7, 89, 23] → 89
Hint: Track the largest number as you loop."""


# list=[12,45,7,89,23]

# ans=max(list)

# print(ans)

"""15. Add an element
Start with numbers = [1, 2, 3]. Add 4 to the end and 0 to the beginning.
Expected output: [0, 1, 2, 3, 4]
Hint: append() and insert()"""


# list1=[1,2,3]
# list1.append(4)
# list1.insert(0,0)
# print(list1)

"""
16. Remove duplicates
Write a function that removes duplicate values from a list.
Example: [1, 2, 2, 3, 1, 4] → [1, 2, 3, 4]
Challenge: Preserve the original order."""

# def fun(num):
#     resu=[]

#     for numers in num:
#         if numers not in resu:
#             resu.append(numers)

#     return resu

# print(fun([1,1,2,2,3,4,4,1]))
def dup(num):
    n=[]
    for nums in num:
        if nums not in n:
            n.append(nums)

    return n

print(dup([1,1,2,3,2,3,4,5,45,1]))
"""17. Separate even and odd numbers
Given [1, 2, 3, 4, 5, 6, 7, 8], create two lists: one for even numbers and one for odd numbers.
Expected output:
Even: [2, 4, 6, 8]
Odd: [1, 3, 5, 7]"""

# def diff(number):
#     even=[]
#     odd=[]
#     for num in number:
#         if num % 2 == 0:
#             even.append(num)
#         else :
#             odd.append(num)
#     return even ,odd
# even ,odd=diff([1,2,3,4,5,6,7,8,9])
# print("even: ",even)
# print("odd: ",odd)


"""18. Find the second-largest number
Write a function that returns the second-largest distinct number.
Example: [10, 20, 20, 8, 15] → 15"""



# def secod_lar(number):

#     original_set=list(set(number))
#     original_set.sort()

#     print(original_set)
#     return original_set[-2]
# print(secod_lar([12,10,12,100,0,12,17,2004,4]))


"""19. Square every number
Use a list comprehension to create a new list containing the square of each number.
Example: [1, 2, 3, 4, 5] → [1, 4, 9, 16, 25"""


# list1=[1,2,3,4,5]

# ans=[num ** 2 for num in list1]
# print(ans)


"""20. Filter passing marks
Given marks = [35, 80, 42, 29, 90, 55], create a list containing only marks greater than or equal to 40.
Expected output: [80, 42, 90, 55]
Hint: List comprehension with an if condition"""



# marks=[35,80,42,29,90,55]

# ans=[mark for mark in marks if mark >=40]
# print(ans)


"""21. Rotate a list
Rotate the list one position to the right.
Example: [1, 2, 3, 4, 5] → [5, 1, 2, 3, 4]"""

# def roted_list(number):
#     return number[-1:]+number[:-1]


# print(roted_list([1,2,3,4,5]))


# list=[1,2,3,4,5]
# print(list[-1:])


"""22. Find common elements
Given:
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

Expected output: [3, 4, 5]"""
# a = [1, 2, 3, 4, 5]
# b = [3, 4, 5, 6, 7]

# # comman= list((set(a)) & (set(b)))
# # print(comman)

# a = [1, 2, 3, 4, 5]
# b = [3, 4, 5, 6, 7]


# coman=[num for num in a if num  in b ]

# for num in  a:
#     if num in b:
#         coman.append(num)
# print(coman)



"""23. Flatten a nested list
Convert [[1, 2], [3, 4], [5, 6]] into [1, 2, 3, 4, 5, 6]."""



# def flatten(nested):
#     result=[]

#     for sublist in nested:
#         for num in  sublist:
#             result.append(num)

#     return result

# nested=[[1,2],[3,4],[5,6]]
# print(flatten(nested))


# def fun(nested):

#     ans=[]

#     for num in nested:
#         for number in num:
#             ans.append(number)

#     return ans       

# nested=[[1,2],[3,4],[5,6]]

# print(fun(nested))
"""
24. Find the most frequent element
Write a function that returns the element appearing most often.
Example: [1, 2, 2, 3, 2, 4, 4] →"""


def count_num(number):
        most_num=number[0]
        max_count=0


        for num in number:
            count=number.count(num)

            if count > max_count:
                max_count=count
                most_num=num

        return most_num   

print(count_num([1, 2, 2, 3, 2, 4, 4]))


def m_count(num):
    max_num=num[0]
    max_count=0

    for nums in num:
        count=num.count(nums)

        if count > max_count:
            max_count=count
            max_num=nums

    return max_num      
 
print(m_count([1, 2, 2, 3, 2, 4, 4]))




# def count_number(number):
#     most_num=number[0]
#     max_count=0

#     for num in number:
#         count=number.count(num)

#         if count > max_count:
#             max_count=count
#             most_num=num
#     return most_num
# print(count_num([1, 2, 2, 3, 2, 4, 4]))
        

"""25. Split a list into chunks
Write a function that splits a list into smaller lists of size 3.
Example:
[1, 2, 3, 4, 5, 6, 7]

[[1, 2, 3], [4, 5, 6], [7]]"""


# list=[1, 2, 3, 4, 5, 6, 7]

# 
# list

"""
Part 3: Mixed String + List Challenges
These are useful because real Python problems often combine both topics.
26. Clean and sort names
Given:
names = [" alice ", "BOB", " charlie", "Alice"]



Remove extra spaces, convert every name to lowercase, remove duplicates, and sort alphabetically.
Expected output:
['alice', 'bob', 'charlie']"""




# def clean_names(names):
#     clean=[]


#     for name in names:
#         clean.append(name.strip().lower())
#     result=sorted(set(clean))

#     return result



# names = [" alice ", "BOB", " charlie", "Alice"]
# print(clean_names(names))


"""

28. Create initials
Given the name "john michael smith", return "J.M.S.".
Hint: split(), indexing, and upper()."""


name="john michael smith"
ans=".".join([word[0].upper() for word in name.split()])+"."
print(ans)


# result=".".join([word[0].upper() for word in name.split()])+"."
# print(result)

"""29. Remove short words
Given "Python is a powerful programming language", return a list of words with at least four characters.
Expected output:
['Python', 'powerful', 'programming', 'language']"""


name="Python is a powerful programming language"
result=[word for word in name.split() if len(word)>4 ]
print(result)