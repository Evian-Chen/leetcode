class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            total += i - nums[i]

        return len(nums) - abs(total) if total != 0 else len(nums)
        