# Day 27
# Maximal Square

# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# Input: 

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# Output: 4

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        rows = len(matrix)
        
        if rows == 0:
            return 0
        
        cols = len(matrix[0])
        
        dp = [[0]*(cols+1) for i in range(rows+1)]
        maxlen = 0
        
        for i in range(rows+1):
            for j in range(cols+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif matrix[i-1][j-1] == "0":
                    dp[i][j] == 0
                elif matrix[i-1][j-1] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                    maxlen = max(maxlen, dp[i][j])
        
        return maxlen*maxlen