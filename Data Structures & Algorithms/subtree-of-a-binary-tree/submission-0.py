# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def comp(node,sub):
            if not node and not sub:
                return True
            if not node or not sub or node.val != sub.val:
                return False
            return comp(node.left, sub.left) and comp(node.right, sub.right)

        def dfs(curr):
            if not curr:
                return False
            if curr.val == subRoot.val:
                if comp(curr,subRoot):
                    return True
            return dfs(curr.left) or dfs(curr.right)

        
        return dfs(root)
