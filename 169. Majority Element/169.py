class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # O(nlogn)
        # nums.sort()
        # return nums[len(nums)//2]

        # O(n)
        d = dict()
        for num in nums:
            d[num] = d[num]+1 if num in d else 1
            if d[num] > len(nums)//2:
                return num