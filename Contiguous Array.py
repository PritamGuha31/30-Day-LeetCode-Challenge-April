# Day 13
# Contiguous Array
# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_len = 0
        sum_nums = 0
        sum_dict = {}
        
        for index in range(0,len(nums)):
            if nums[index] == 0:
                sum_nums = sum_nums - 1
            else:
                sum_nums += 1
            
            if sum_nums == 0:
                max_len = index + 1
            
            if sum_nums in sum_dict:
                if max_len < index - sum_dict[sum_nums]:
                    max_len = index - sum_dict[sum_nums]
            else:
                sum_dict[sum_nums] = index
        
        return max_len
            