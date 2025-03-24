class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        greater = False
        for num in nums1:
            ind = nums2.index(num)
            num2 = nums2[ind]

            for i in range(ind + 1, len(nums2)):
                if nums2[i] > num2:
                    ans.append(nums2[i])
                    greater = True
                    break
            if not greater:
                ans.append(-1)
            greater = False
            
        return ans

        