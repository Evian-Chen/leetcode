class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        times = 0
        for i in range(len(nums)):
            if total == 0 and nums[i] != 0:
                total += nums[i]
                times += 1
            else:
                if nums[i]-total != 0:
                    times += 1
                    total += nums[i]-total
        return times

