# Day 19
# Search Rotated Sorted Array
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.
# Your algorithm's runtime complexity must be in the order of O(log n).

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Using Modified Binary Search

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if nums == None or len(nums)==0 :
            return -1
        
        left = 0
        right = len(nums)-1
        
        while left < right:
            middle = left + (right-left) / 2
            if nums[middle] > nums[right]:
                left = middle + 1
            else :
                right = middle
        
        start = left
        left = 0
        right = len(nums)-1
        
        if target >= nums[start] and target <= nums[right] :
            left =  start
        else :
            right = start
        
        while left <= right:
            middle = left + (right-left) / 2
            if target > nums[middle]:
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1
            else:
                return middle
        
        return -1