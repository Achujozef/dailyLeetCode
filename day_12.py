from typing import List
class Solution:
    
    def removeDuplicates(self, nums: List[int]) -> int:
        unique=[]
        for num in nums:
            if num not in unique:
                unique.append(num)
        nums[:]=unique
        print(nums)
        return len(nums)

nums=[1,1,2]  
x=Solution()
m=x.removeDuplicates(nums)
print(m)