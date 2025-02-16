class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        longer, shorter = (nums2, nums1) if len(nums1) < len(nums2) else (nums1, nums2)
        for i in range(len(shorter)):
            if shorter[i] in longer and shorter[i] not in ans:
                ans.append(shorter[i])
        return ans