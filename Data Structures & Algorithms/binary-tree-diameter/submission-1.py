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
        self.traverse(root)
        return self.max_diameter

    


    def traverse(self,node):
        if not node:
            return 
    
        left_depth = self.depth(node.left)
        right_depth = self.depth(node.right)
        self.max_diameter = max(self.max_diameter,left_depth + right_depth)
        
        self.traverse(node.left)
        self.traverse(node.right)

        



    def depth(self,node):
        if not node:
            return 0

        left_depth = self.depth(node.left)
        right_depth = self.depth(node.right)

        return max(left_depth,right_depth) + 1


        