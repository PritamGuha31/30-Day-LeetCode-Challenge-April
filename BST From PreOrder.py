# Day 20
# Construct Binary Search Tree from Preorder Traversal
# Return the root node of a binary search tree that matches the given preorder traversal.
# Recall that a binary search tree is a binary tree where for every node, 
# any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  
# Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.

# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        inorder = sorted(preorder)
        return self.createTree(preorder,inorder)
    
    def createTree(self,preorder,inorder):
        
        if len(preorder) != len(inorder) or preorder is None or inorder is None or len(preorder) == 0 :
            return None
        
        preorderlen = len(preorder)
        inorderlen = len(inorder)
        
        root = TreeNode(preorder[0])
        rootindex = inorder.index(root.val)
        
        root.left = self.createTree(preorder[1:rootindex+1], inorder[:rootindex])
        root.right = self.createTree(preorder[rootindex+1:], inorder[rootindex+1:])
        
        return root