class Solution(object):
    def romanToInt(self, s):
        n=0
        
        for i in range(len(s)-1):
            if s[i-1]=='I':
                x=self.romanToInthlpr(s[i])
                n=n+(x-1)
            elif s[i-1]=='X':
                x=self.romanToInthlpr(s[i])
                n=n+(x-10)
            elif s[i-1]=='C':
                x=self.romanToInthlpr(s[i])
                n=n+(x-100)
            else:
                x=self.romanToInthlpr(s[i])
                n=n+x
                
        return n
    def romanToInthlpr(self, s):
        switch={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        return switch.get(s,"Invalid Input")
x=Solution()

print(x.romanToInt('MCMXCIV'))