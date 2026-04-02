# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        rt = root
        while not (p.val <= rt.val <= q.val) and not (p.val >= rt.val >= q.val):
            if rt.val > q.val and rt.left:
                rt = rt.left
            elif rt.val < p.val and rt.right:
                rt = rt.right
            
        return rt
        # def dfs(rt):
        #     if (p.val <= rt.val and rt.val <= q.val): #or (q.val < rt.val and rt.val < p.val):
        #         return rt
        #     elif p.val > rt.val and rt.left:
        #         return dfs(rt.left)
        #     elif rt.right:
        #         return dfs(rt.right)
        #     return rt
        # return dfs(root)