# Day 23
# Bitwise AND of Numbers Range

# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

# Input: [5,7]
# Output: 4

# Input: [0,1]
# Output: 0

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        result = 0
        
        while(m > 0 and n > 0):
            x = self.getMSB(m)
            y = self.getMSB(n)
            
            if (x != y):
                break
            
            result = result + (2**x)
            
            m = m - (2**x)
            n = n - (2**x)
        
        return result
    
    def getMSB(self, x):
        
        msb = -1
        while(x > 0):
            x = x >> 1
            msb += 1
        
        return msb
        
        