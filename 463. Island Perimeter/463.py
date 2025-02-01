class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        per = 0
        # i 直向 j 橫向

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:  # land
                    # left
                    if j-1 == -1 or (j-1 >= 0 and grid[i][j-1] == 0):  # 最左邊的格子
                        per += 1
                    # right
                    if j+1 == len(grid[i]) or (j+1 < len(grid[i]) and grid[i][j+1] == 0):  # 最右邊的格子
                        per += 1
                    # up
                    if i-1 == -1 or (i-1 >= 0 and grid[i-1][j] == 0):  # 最上面的
                        per += 1
                    # down
                    if i+1 == len(grid) or (i+1 < len(grid) and grid[i+1][j] == 0):
                        per += 1
        return per