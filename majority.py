from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int: 
        majority =None
        count = 0
        for num in nums:
            if count == 0:
                majority=num
            if num == majority:
                count +=1
            else:
                count -=1
        return majority
        

                

nums = [2,2,1,1 ,1,2 ,2,1 ,1,2]
x=Solution()
m=x.majorityElement(nums)
print(m)