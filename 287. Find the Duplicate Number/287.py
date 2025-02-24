class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        history = set()
        for num in nums:
            if num in history:
                return num
            history.add(num)