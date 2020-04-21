# Day 21
# Leftmost Column with at Least a One

# A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

# Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. 
# If such index doesn't exist, return -1.

# You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

# BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
# BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.
# Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  
# Also, any solutions that attempt to circumvent the judge will result in disqualification.

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x, y):
#        """
#        :type x : int, y : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        dimensions = binaryMatrix.dimensions()
        
        return self.leftMostOne(0,dimensions[1]-1,dimensions,-1,binaryMatrix)
    
    def leftMostOne(self,i,j,dimensions,currentVal,binaryMatrix):
        if i < 0 or i >= dimensions[0] or j < 0 or j >= dimensions[1]:
            return currentVal
        
        
        if binaryMatrix.get(i,j) == 1:
            return self.leftMostOne(i,j-1,dimensions,j,binaryMatrix)
        else:
            return self.leftMostOne(i+1,j,dimensions,currentVal,binaryMatrix)