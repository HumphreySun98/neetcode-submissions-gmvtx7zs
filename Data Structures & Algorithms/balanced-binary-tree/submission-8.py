# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        self.depth(root)
        return self.balanced
        

        


    def depth(self,node):
        if not node:
            return 0

        left_depth = self.depth(node.left)
        right_depth = self.depth(node.right)


        if abs(left_depth - right_depth) > 1:
            self.balanced = False

        return max(left_depth,right_depth) +1
        