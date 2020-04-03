# Day 1
# Single Number
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Input: [2,2,1]
# Output: 1

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numCount = {}
        for num in nums:
            if num in numCount.keys():
                numCount[num] = numCount[num]+1
            else:
                numCount[num] = 1
        
        for key,value in numCount.items():
            if value == 1:
                return key
        