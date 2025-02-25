class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_index.append(i)
            else:
                if zero_index:
                    nums[zero_index[0]] = nums[i]
                    nums[i] = 0
                    zero_index.pop(0)
                    zero_index.append(i)
        