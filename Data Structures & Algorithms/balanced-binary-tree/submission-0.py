# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.valid = True
        def dfs(curr):
            if not curr:
                return 0
            l,r = dfs(curr.left), dfs(curr.right)
            if abs(l-r)>1:
                self.valid = False
            return max(l,r)+1

        dfs(root)
        return self.valid

                    