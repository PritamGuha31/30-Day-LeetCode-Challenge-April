# Day 18
# Minimum Path Sum
# Given a m x n grid filled with non-negative numbers, 
# find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Input:
# [
#  [1,3,1],
#  [1,5,1],
#  [4,2,1]
#]
# Output: 7
# Explanation: Because the path 1?3?1?1?1 minimizes the sum.

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sumGrid = []
        
        for i in range(len(grid)):
            sumGrid.append([])
            for j in range(len(grid[i])):
                sumGrid[i].append(grid[i][j])
                
                if i > 0 and j > 0 :
                    sumGrid[i][j] += min(sumGrid[i-1][j], sumGrid[i][j-1])
                elif i > 0:
                    sumGrid[i][j] += sumGrid[i-1][j]
                elif j > 0:
                    sumGrid[i][j] += sumGrid[i][j-1]
        
        return sumGrid[len(grid)-1][len(grid[0])-1]
                    