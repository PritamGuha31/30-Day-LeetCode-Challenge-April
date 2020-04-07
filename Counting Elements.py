# Day 7
# Counting Elements
# Given an integer array arr, count element x such that x + 1 is also in arr.
# If there're duplicates in arr, count them seperately.

# Input: arr = [1,2,3]
# Output: 2
# Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

# Input: arr = [1,1,3,3,5,5,7,7]
# Output: 0
# Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.

# Input: arr = [1,3,2,3,5,0]
# Output: 3
# Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.

# Input: arr = [1,1,2,2]
# Output: 2
# Explanation: Two 1s are counted cause 2 is in arr.

class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        duplicatesRemoved = []
        count = 0
        arr = sorted(arr)
        i = 0
        index = 0
        
        for num in arr:
            if num not in duplicatesRemoved :
                duplicatesRemoved.append(num)
        
        for index in range(len(arr)):
            if arr[index] + 1 in duplicatesRemoved :
                count = count + 1
        
        return count