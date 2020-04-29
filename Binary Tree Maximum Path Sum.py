# Day 29
# Binary Tree Maximum Path Sum

# Given a non-empty binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 
# The path must contain at least one node and does not need to go through the root.

# Input: [1,2,3]

#       1
#      / \
#     2   3

# Output: 6

# Input: [-10,9,20,null,null,15,7]

#   -10
#   / \
#  9  20
#    /  \
#   15   7

# Output: 42

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum = float("-inf")
        
        def pathSum(root):
            if root is None:
                return 0
            left = max(0, pathSum(root.left))
            right = max(0, pathSum(root.right))
            self.maxSum = max(self.maxSum, left + right + root.val)
        
            return max(left, right) + root.val
        
        pathSum(root)
        return self.maxSum
    
    