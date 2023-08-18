class Solution(object):
    def isValid(self, s):
       for i in range(len(s)):
            
                
            if i%2==0:
               s[i]==s[i-1]
               x=True
            else:
               x=False
       return x
               