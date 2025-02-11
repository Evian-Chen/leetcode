class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        else:
            maxi = 0
            for i in range(len(s)):
                sub = ""
                # if s.find(s[i], i+1, len(s))-i > maxi:
                for ch in s[i:]:
                    if ch not in sub:
                        sub += ch
                    else:
                        break
                if len(sub) > maxi:
                    maxi = len(sub)
            return maxi