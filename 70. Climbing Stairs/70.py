class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}
        return self.helper(n, memo)

    def helper(self, n, memo):
        if n in memo:
            return memo[n]
        else:
            memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
            return memo[n]
            