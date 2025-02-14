# hint: Every number N can be written as product of prime numbers as
# N = (A^a)(B^b)(C^c)....

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        if n in [1, 2, 3, 5]:
            return True
        else:
            while True:
                if n % 2 == 0:
                    n /= 2
                elif n % 3 == 0:
                    n /= 3
                elif n % 5 == 0:
                    n /= 5
                else:
                    if n == 1:
                        return True
                    else: 
                        return False

        