# Day 17
# Number of Islands
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    count += 1
                    self.callBfs(grid,i,j)
        
        return count
    
    def callBfs(self,grid,i,j):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[i]) or grid[i][j]=='0' :
            return
        
        grid[i][j] = '0'
        self.callBfs(grid,i-1,j)
        self.callBfs(grid,i+1,j)
        self.callBfs(grid,i,j+1)
        self.callBfs(grid,i,j-1)