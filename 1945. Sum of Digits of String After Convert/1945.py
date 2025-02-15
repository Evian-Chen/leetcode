# ord(), 'a'->97

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        new_s = ""
        for ascii in s:
            num = ord(ascii) - 96
            new_s += str(num)
        
        for i in range(k):
            total = 0
            for num in new_s:
                total += int(num)
            new_s = str(total)
        return total