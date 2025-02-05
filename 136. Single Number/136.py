class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]
        # else:
        #     for i in range(len(nums)-1):
        #         if nums[i] not in nums[i+1:] and nums[i] not in nums[:i]:
        #             return nums[i]
        #     return nums[-1]

        # using bitwise XOR
        ans = 0
        for num in nums:
            ans ^= num
        return ans