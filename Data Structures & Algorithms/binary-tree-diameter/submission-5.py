# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        self.max_diameter = 0

        self.dfs(root)

        return self.max_diameter



    def dfs(self,node):
        if not node:
            return 0

        left_depth = self.dfs(node.left)
        right_depth = self.dfs(node.right)

        self.max_diameter = max(self.max_diameter,left_depth + right_depth)

        return max(left_depth,right_depth) +1
        