class Solution:
    def longestPalindrome(self, s: str) -> str:
        history = set()
        cur = ""
        max_p = ""
        for i in range(len(s)):
            cur = s[i]
            history.add(cur)
            
            for j in range(i+1, len(s)):
                cur += s[j]
                if self.isPalinfrom(cur, history):
                    history.add(cur)
                    if len(cur) >= len(max_p):
                        max_p = cur
        return cur if not max_p else max_p
                    
    def isPalinfrom(self, s, history):
        if s in history:
            return True
        front, end = 0, len(s)-1
        while front <= end:
            if s[front] == s[end]:
                front += 1
                end -= 1
            else:
                return False
        return True
            