class Solution:
    def intToRoman(self, num: int) -> str:
        d = [(1000, 'M'), (500, 'D'), (100, 'C'), (50, 'L'), (10, 'X'), (5, 'V'), (1, 'I')]
        r = "MDCLXVI"
        ans = ''

        for integer, roman in d:
            a = num//integer

            if a > 3:
                if len(ans) != 0 and r[r.find(roman)-1] == ans[-1]:  # 9
                    temp = r[r.find(roman)-2]
                    ans = ans[:-1]
                else: 
                    temp = r[r.find(roman)-1]
                
                ans += (roman + temp)
            else:
                ans += a*roman

            num %= integer
        
        return ans