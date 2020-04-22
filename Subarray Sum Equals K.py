# Day 22
# Subarray Sum Equals K

# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

# Input:nums = [1,1,1], k = 2
# Output: 2

from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        sumDict = defaultdict(int)
        sumNum = 0
        count = 0
        
        sumDict[0] = 1
        
        for i in range(len(nums)):
            sumNum = sumNum + nums[i]
            
            if sumDict.get(sumNum - k) > 0:
                count += sumDict.get(sumNum-k)
            
            sumDict[sumNum] += 1
        
        return count