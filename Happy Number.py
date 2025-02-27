# Day 2
# Happy Number
# Write an algorithm to determine if a number is "happy".
# Starting with any positive integer, replace the number by the sum of the squares of its digits, 
# and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
# Those numbers for which this process ends in 1 are happy numbers.

# Input: 19
# Output: true
# Explanation: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

class Solution(object):
    
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = {}
        
        while(n!=1):
            n = str(n)
            l = list(n)
            l = list(map(int,l))
            sumsquare = 0
            for i in l:
                sumsquare = sumsquare + (i**2)
            
            if visited.has_key(sumsquare):
                return False
            
            visited[sumsquare] = 1
            
            n = sumsquare
        
        return True
                                
            
        
        
        
            
            
        