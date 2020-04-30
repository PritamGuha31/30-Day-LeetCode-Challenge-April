# Day 30
# Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree

# Given a binary tree where each path going from the root to any leaf form a valid sequence, 
# check if a given string is a valid sequence in such binary tree. 

# We get the given string from the concatenation of an array of integers arr and 
# the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.

# Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
# Output: true
# Explanation: 
# The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure). 
# Other valid sequences are: 
# 0 -> 1 -> 1 -> 0 
# 0 -> 0 -> 0

# Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
# Output: false 
# Explanation: The path 0 -> 0 -> 1 does not exist, therefore it is not even a sequence.

# Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
# Output: false
# Explanation: The path 0 -> 1 -> 1 is a sequence, but it is not a valid sequence.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidSequence(self, root, arr):
        """
        :type root: TreeNode
        :type arr: List[int]
        :rtype: bool
        """
        
        index = 0
        node = root
        
        return self.checkValidSequence(root, arr)
    
    def checkValidSequence(self, node, arr):
        if node is None :
            return len(arr) == 0
        
        if (len(arr)==1) and node.val == arr[0] and (node.left == None and node.right == None):
            return True
        elif len(arr) > 1 and node.val == arr[0]:
            return (self.checkValidSequence(node.left, arr[1:])) or (self.checkValidSequence(node.right, arr[1:]))