class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1, p2 = 0, len(height)-1
        maxi, total = 0, 0
        finalIndex = (p1, p2)
        while (p2 > p1):
            
            total = (p2 - p1) * min(height[p1], height[p2])
            if (total > maxi):
                maxi = total
                finalIndex = (p1, p2)
            if (height[p1] < height[p2]):
                p1 += 1
            else:
                p2 -= 1
        return maxi