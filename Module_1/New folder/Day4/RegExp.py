"It is a pattern used to search ,extract, validate, or replace text"
"{1} use the exactly number"
"^ use the startig line "
"[] use for find the group like [1-9],[A-Z]"


import re

# text="My phone number is 9456789040"
# result=re.search(r"\d+",text)
# print(result.group())


"with the use of r'my' find the string"
# result1=re.search(r"My",text)
# print(result1.group())


# find1=re.match(r"My",text)
# print(find1.group())


"Findall methdo to use the final all in string"

# string="Hello my Name is 123 and my age is 1_2-34"
# str=re.match(r"\w",string)
# print(str.group())
# ans=re.findall(r"\w",string)
# print(ans)

"sub method to use the replace string"

# answer=re.sub(r"123","Dax",string)
# print(answer)



"[]  use the any character from the string"


# string="Hello my Name is 123 and my age is 1_2-34"

# print(re.findall(r"^Hello",string))
# print(re.findall(r"[aeiou,0-9,A-Z]",string))












phone="9157066286"
name="Hello Good Morning"

ans1=re.search(r"^Hello.*Morning$",name)
print(ans1.group())

ans=re.findall(r"^[0-9]\d{9}$",phone)
print(ans)


import re
txt = 'The rain in Spain'
x = re.search('a', txt)
print(x.start())