# Day 3
# Maximum Subarray - Given an integer array nums, find the contiguous subarray 
# (containing at least one number) which has the largest sum and return its sum.
# Input: [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Divide and Conquer Approach
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.solve(nums,0,len(nums)-1)
    
    def solve(self,nums,l,r):
        
        if l==r:
            return nums[l]
        
        m = (l+r)//2
        
        return max(self.solve(nums,l,m), self.solve(nums,m+1,r), self.maxCrossSum(nums,l,m,r))
    
    def maxCrossSum(self,nums,l,m,r):
        
        tempSum = 0
        maxLeftSum = nums[m]
        
        for index in range(m,l-1,-1):
            tempSum = tempSum + nums[index]
            if tempSum > maxLeftSum:
                maxLeftSum = tempSum
        
        tempSum = 0
        maxRightSum = nums[m+1]
        
        for index in range(m+1,r+1):
            tempSum =tempSum + nums[index]
            if tempSum > maxRightSum:
                maxRightSum = tempSum
        
        return maxLeftSum + maxRightSum