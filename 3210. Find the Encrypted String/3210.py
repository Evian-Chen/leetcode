class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        ans = ""
        for i in range(len(s)): 
            index = i + k
            while index >= len(s)-1:
                index -= len(s) 
            ans += s[index]
        return ans