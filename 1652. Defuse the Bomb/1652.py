class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        if k > 0:
            ans = []
            for i in range(len(code)):
                ans.append(sum(code[(n+i) % len(code)] for n in range(1, k+1)))
            return ans
        if k < 0:
            ans = []
            for i in range(len(code)):
                ans.append(sum(code[(i-n) % len(code)] for n in range(1, -k+1)))
            return ans