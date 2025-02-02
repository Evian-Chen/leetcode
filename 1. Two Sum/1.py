class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            new_t = target - nums[i]
            if i+1 == len(nums)-1:
                return [i, i+1]
            if new_t in nums[i+1:]:
                return [i, nums[i+1:].index(new_t)+i+1]
