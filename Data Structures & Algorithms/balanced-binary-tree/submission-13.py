# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = 0
        self.balance = True

        def dfs(node):
            if not node:
                return 0

            res_left = dfs(node.left)
            res_right = dfs(node.right)


            self.res = abs(res_left - res_right)
            if self.res > 1:
                self.balance = False
            return 1+max(res_left, res_right)


        dfs(root)
        return self.balance



        
            


        


        