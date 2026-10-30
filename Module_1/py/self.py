# # attemp=5
# # while attemp >0:
# #     pin=input()

# #     if pin == "12":
# #         print("Done")
# #         break

# #     attemp=attemp-1

# #     print(f"wronge {attemp} left")

# # else:
# #     print("looked")


# # list=[12,11,10,9,8]

# # output =[11,10,9,8,7]
# """class Solution:
#     def dercementArray(self, arr: list[int], n: int) -> list[int]:
#         return [x - 1 for x in arr]"""

# # class Solution:
# #     def dercementArray(self,arr:list[int],n:int):

# #         return[]



# """
# class hello:
#     def diff(self,arr):
#         ans=list(arr)

#         d=arr[1]-arr[0]


#         for _ in range(13):
#             ans.append(ans[-1]+d)   
#         return ans
# arr=[1,3,5,7,9]
# h1=hello()
# print(h1.diff(arr))"""



# # Taking input and initializing dictionary
# keys = input().split()
# values = map(int, input().split())
# my_dict = dict(zip(keys, values))
# k, v = input().split()

# ########### Write your code below ###############
# # Insert k,v in my_dict
# # Print Inserted if inserted successfuly

# my_dict[k]=int(v)
# print("Inserted")
# ########### Write your code above ###############

# d = input()

# ########### Write your code below ###############
# # Delete entry with key d from my_dict
# # Print Deleted if deleted successfuly else print -1
# if d in my_dict:
#     del my_dict[d]
#     print("Deleted")
# else:
#     print("-1")

# ########### Write your code above ###############

# p = input()

# ########### Write your code below ###############
# # Print marks of given key p if key present, else print -1

# if p in my_dict:
#     print("Marks of " + p + " is " + str(my_dict[p]))
# else:
#     print("-1")
# ########### Write your code above ###############




a="10"
b="10"

class Solution:
    def findsum(self,s1,s2):
        num=int(s1)
        num1=int(s2)

        return num + num1

a1=Solution()
print(a1.findsum(10,20))
