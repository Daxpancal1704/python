"Longest subarray with sum k "

class Solution:
    def longsubarrayk(self,arr,k):
        pre_fix=0
        max_line=0
        seen={0:-1}

        for i in range(len(arr)):
            pre_fix +=  arr[i]

            if (pre_fix - k) in seen:
                max_line=max(max_line,i-seen[pre_fix - k])

            if pre_fix not in seen:
                seen[pre_fix] = i

        return max_line

arr=[1,2,3,4,5,6,7,8,9]
k=10

s1=Solution()
print(s1.longsubarrayk(arr,k))