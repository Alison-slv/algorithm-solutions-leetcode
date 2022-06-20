# problem: 2236 Root Equals Sum Of Children
# dufficulty: easy
# -----------------------------------------
# You are given the root of a binary tree that consists of exactly 3 nodes: the root, its left child, and its right child.
# Return true if the value of the root is equal to the sum of the values of its two children, or false otherwise.
# Input: root = [10,4,6]
# Output: true
# Explanation: The values of the root, its left child, and its right child are 10, 4, and 6, respectively.
# 10 is equal to 4 + 6, so we return true.


# Definition for a binary tree node.
#class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == root.left.val + root.right.val:
            return True
        else:
            return False


print(Solution().checkTree([5, 3, 1]))
