# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.valid = True
        def dfs(a,b):
            if not a and not b:
                return
            
            if not a or not b or a.val != b.val:
                self.valid=False
                return
            dfs(a.left, b.left)
            dfs(a.right, b.right)
            return

        dfs(p,q)
        return self.valid