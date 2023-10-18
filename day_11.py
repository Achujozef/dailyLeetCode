# class Solution(object):
#     def removeElement(self, nums, val):
#         nums=[num for num in nums if num !=val]
#         return len(nums)
class Solution:
    def removeElement(self, nums, val) -> int:
        nums=[num for num in nums if num !=val]
        print(nums)
        return len(nums)
nums=[3,2,2,3]
x=Solution()
m=x.removeElement(nums,3)
print(m)
