# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)

        diff = abs(left_depth - right_depth)

        if diff > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)


    def depth(self,node):
        if not node:
            return 0

        left_depth = self.depth(node.left)
        right_depth = self.depth(node.right)


        return max(left_depth,right_depth) + 1


        