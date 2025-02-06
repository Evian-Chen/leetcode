class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                t = -nums[i]
                k = len(nums)-1
                j = i + 1
                
                while j < k:
                    if nums[j] + nums[k] > t:
                        k -= 1
                    elif nums[j] + nums[k] < t:
                        j += 1
                    else:
                        ans.append([nums[i], nums[j], nums[k]])
                        j += 1
                        while nums[j] == nums[j-1] and j < k:
                            j += 1
        return ans