# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        count = 1
        current_left = 0
        current_right = 0
        if root.left:
            current_left += 1
        if root.right:
            current_right += 1
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1