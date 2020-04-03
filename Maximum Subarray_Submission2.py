# Day 3
# Maximum Subarray - Given an integer array nums, find the contiguous subarray 
# (containing at least one number) which has the largest sum and return its sum.
# Input: [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

#Kadane's Algo
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxSum = currentSum = nums[0]
        
        for i in range(1,len(nums)):
            currentSum = max(nums[i],currentSum + nums[i])
            if currentSum > maxSum:
                maxSum = currentSum
        
        return maxSum
        
        