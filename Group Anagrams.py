# Day 6
# Group Anagrams
# Given an array of strings, group anagrams together.
# ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [
#  ["ate","eat","tea"],
#  ["nat","tan"],
#  ["bat"]
# ]

from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        myDict = defaultdict(list)
        
        for index in range(len(strs)):
            splitString = list(strs[index])
            sortedSplitString = ''.join(sorted(splitString))
            myDict[sortedSplitString].append(strs[index])
            
        myAnagramList = []
        
        for key, value in myDict.items():
            myAnagramList.append(value)
        
        return myAnagramList