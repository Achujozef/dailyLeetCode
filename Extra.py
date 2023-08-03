class Solution(object):
    def longestCommonPrefix(self, strs):
        largest=''
        for i in range(len(strs)):
            for j in range(len(strs)):
                if strs[i]==strs[j] and len(strs[j])> len(largest):
                    largest=strs[j]
        return largest


strs=['Achu','ACHU','Jozef','Achu','Jozef']

x=Solution()
print(x.longestCommonPrefix(strs))