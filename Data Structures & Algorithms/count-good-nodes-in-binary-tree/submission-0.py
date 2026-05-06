# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0

        def dfs(node, maxparent):
            nonlocal good

            if not node:
                return True
            print(good, node.val, maxparent)
            if node.val>=maxparent:
                good+=1
            dfs(node.left,max(maxparent, node.val))
            dfs(node.right,max(maxparent, node.val))
            
            return True



        dfs(root, root.val)

        return good
