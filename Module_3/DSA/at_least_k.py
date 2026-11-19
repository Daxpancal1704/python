"At least k occurrences"

class solution:
    def atleastl(self,arr,k):
        count={}

        for num in arr:
            count[num]=count.get(num,0)+1

            if count[num] == k:
                return num
        
        return -1
arr=[1,2,3,4,1,23,4,1,23,4]
k=2

s1=solution()
print(s1.atleastl(arr,k))
