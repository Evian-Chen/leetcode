class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1)-1, len(num2)-1
        total, carry = 0, 0
        ans = ""
        while i >= 0 or j >= 0:
            total += int(num1[i]) if i >= 0 else 0
            total += int(num2[j]) if j >= 0 else 0
            total += carry
            carry = 0
            if total >= 10:
                carry = 1
                total -= 10
            ans = str(total) + ans
            total = 0
            i -= 1
            j -= 1
        if carry != 0:
            return "1"+ans
        return ans

        