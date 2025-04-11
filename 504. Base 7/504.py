class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        ans = "" if num > 0 else "-"
        num = abs(num)
        
        total = 0
        hitghest_bit = 0
        while num >= pow(7, hitghest_bit):
            hitghest_bit += 1
        hitghest_bit -= 1

        print(hitghest_bit)
        for i in range(hitghest_bit, -1, -1):
            print(num)
            bit = 0
            for j in range(7):
                if j * pow(7, i) > num:
                    bit = j-1
                    break
                elif j * pow(7, i) == num:
                    bit = j
                    break
                else: 
                    bit = j
            num -= bit * pow(7, i)
            ans += str(bit)

        return ans
        