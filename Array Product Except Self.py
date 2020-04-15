# Day 15
# Product of Array Except Self
# Given an array nums of n integers where n > 1,  
# return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Input:  [1,2,3,4]
# Output: [24,12,8,6]

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftProd = []
        rightProd = []
        
        prod = 1
        
        for num in nums:
            leftProd.append(prod)
            prod = prod * num
        
        prod = 1
        
        for index in range(len(nums)-1,-1,-1):
            rightProd.append(prod)
            prod = prod * nums[index]
        
        rightProd.reverse()
        
        prod = []
        
        for index in range(len(leftProd)):
            prod.append(leftProd[index]*rightProd[index])
        
        return prod