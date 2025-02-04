class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        else:
            total = 0
            history = set()
            while n not in history:
                history.add(n)
                while n != 0:
                    total += (n%10)**2
                    n = n // 10
                if total == 1:
                    return True
                n = total
                total = 0
            return False