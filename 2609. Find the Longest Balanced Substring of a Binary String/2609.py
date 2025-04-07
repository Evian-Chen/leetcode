class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        maxi = 0
        zero_count = 0
        one_count = 0
        first = True
        for digit in s:
            if digit == "0":
                maxi = max(min(zero_count, one_count), maxi)
                if first:
                    zero_count = 0
                    one_count = 0
                    first = False
                zero_count += 1
            else:
                if not first: 
                    first = True
                one_count += 1
            # print(temp_count)
        print(zero_count, one_count)
        maxi = max(min(zero_count, one_count), maxi)
        return maxi*2