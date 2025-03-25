class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ans = []
        for i in range(len(nums)):
            if nums[i] not in ans:
                if len(ans) < 3:
                    ans.append(nums[i])
                    ans.sort(reverse=True)
                else:
                    if nums[i] >= ans[-1]:
                        ans.pop()
                        ans.append(nums[i])
                        ans.sort(reverse=True)
        if len(ans) == 3:
            return ans[-1]
        else:
            return ans[0]