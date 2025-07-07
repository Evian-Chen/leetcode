class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            if len(res) < k:
                res.append(nums[i])
            else:
                if (max(res) <= nums[i] or min(res) <= nums[i]):
                    res.pop(res.index(min(res)))
                    res.append(nums[i])

        return res