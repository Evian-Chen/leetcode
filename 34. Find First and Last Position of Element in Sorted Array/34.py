class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        if not nums:
            return ans
        else:
            for i in range(len(nums)):
                if nums[i] == target:
                    if ans[0] == -1:
                        ans = [i, i]
                    else:
                        ans[1] = i
                if nums[i] > target:
                    return ans 
            return ans
