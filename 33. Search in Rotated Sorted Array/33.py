class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if self.helper(nums, target):
            return nums.index(target)
        else:
            return -1
        # return self.helper(nums, target)

    def helper(self, nums, target):
        if len(nums) == 1:
            if target == nums[0]:
                return True
            else:
                return False
        else:
            return self.helper(nums[:len(nums)//2], target) or self.helper(nums[len(nums)//2: ], target)