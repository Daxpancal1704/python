# # # import re

# # # string="""Explanation: re.search(r'portal', txt) finds the first occurrence of "portal" in the string. match.group() returns "portal", start() is 34 and end() is 40 (spaces included in count)."""
# # # search=re.search(r'portal',string)

# # # # group() -> use for find the char name in string  
# # # print(search.group())



# # # if search:
# # #     print(search.group())
# # #     #search.start() -> use for find the index to start number  &  search.end() -> use for find the index to end number  
# # #     print("start :",search.start(),"end : ",search.end())
# # # else:
# # #     print("Not found")



# # # #finadall("at",string) -> use to find char or string
# # # txt=re.findall("at",string)
# # # print(txt)

# # # #re.search('\s',string) -> use to search for '\s' search whitespace chaeacters index
# # # se=re.search('\s',string)
# # # print("The firstr white space char : ",se.start() )


# # # #used to split character for some chuncks
# # # sp=re.split("\s",string)
# # # print("starting ",sp)


# # # #used to add any char or digit after whitespace
# # # subs=re.sub("\s","17",string)
# # # #use for only 2 time dd char or digit add after whitespace
# # # sub=re.sub("\s","17",string,2)
# # # print(subs)
# # # print()
# # # print(sub)




# # # # searching for digit for whole string also use for [A-Z][a-z]
# # # search_num=re.findall("[0-9]",string)
# # # print(search_num)


# # # # 1.re.match() -> heck weather pattern matches at the beginning of the string
# # # text="Hello,10 Good 22Morning11111 How are 234567You"
# # # reasult=re.match("Hello",text)
# # # print(reasult.group())


# # # # 2.re.search() -> search for the first matching  pattern  anywhere in string 

# # # search=re.search("Good",text)
# # # print(search.group())


# # # #re.findall() -> find all the matching value and return  them in list if use [0-9]+ '+' so find in gruppwise like find digit in group and without '+' get a sing single digit

# # # find=re.findall("[0-9]+",text)
# # # print("find number : ",find)


# # # #re.finditer() -> for find patter for the iter 
# # # ans=re.finditer("[0-9]+",text)
# # # print()
# # # for i in ans:
# # #     print(i.group())

# # # #re.split() -> used  for split the string
# # # split=re.split("[,;]",text)
# # # print(split)

# # # #re.sub()-> use for replace the matching text 

# # # txt="I love UK"
# # # res=re.sub("UK","india",txt)
# # # print(res)

# # # #re.fullmatch() 

# # # num="1233423322323432345678909876543234567"

# # # match=re.fullmatch("[0-9]+",num)
# # # print(match.group().isdigit())
# # # if match:
# # #     print("valid")
# # # else:
# # #     print("not valid")

# # import re
# # texts="ab c1 23 NJE xyECJEVYE z456"


# # #find digit for text it is simple way but use the symbol
# # print(re.findall("[0-9]",texts))

# # # \d  -> use for find digit
# # print(re.findall("\d+",texts))

# # #\w -> use for find word
# # str="python is very easy language"
# # print(re.findall(r"\w+",str))

# # print(re.findall(r"[A-Z]+",texts))




# # #{9}  -> it means exactly 9 more digit
# # mobile="9157066286"


# # if re.fullmatch(r"[0-9]\d{9}",mobile):
# #     print("Number is valid")
# # else:
# #     print("Not valid")


# # email="Hello good morning this is my email addess daxp170@gmial.com"

# # eml=re.findall(r"[\w.-]+@[\w.-]+\.\w+",email)
# # # [\w.-]+@[\w.-]+\.\w+
# # print(eml)


# # emails="jcbbur helo@gmial.com hello sxdgfcvbhnjmk,l;mknjhb"
# # find=re.findall(r"[\w.]+@[\w.-]+",emails)
# # print(find)

# import re

# # 1. Compile the pattern using a raw string (r"...")
# pattern = re.compile(r'\d+')

# # 2. Use the compiled object to search or match text
# match = pattern.search("The order number is 45812.")

# if match:
#     print(match.group())  # Output: 45812


import re

pattern=re.compile(r"\d")
text="i have some number 122122 so it's correct"

result=pattern.findall(text)
print(result)

