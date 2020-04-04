# Day 4
# Move Zeroes 
# Given an array nums, write a function to move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements.
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        countZero = 0
        index = 0
        
        for i in range(len(nums)):
            if nums[i] == 0 :
                countZero = countZero + 1
            else :
                nums[index]  = nums[i]
                index = index + 1
        
        for i in range(countZero):
            nums[len(nums)-1-i] = 0