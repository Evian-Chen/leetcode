class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        for _ in range(len(s)):
            if s[0] not in goal: 
                return False
            new_s = s[1:] + s[0]
            
            if goal == new_s:
                return True
            s = new_s
        return False