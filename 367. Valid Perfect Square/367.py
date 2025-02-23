class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        ans = 1
        while ans * ans <= num:
            if ans * ans == num:
                return True
            ans += 1
        return False
        