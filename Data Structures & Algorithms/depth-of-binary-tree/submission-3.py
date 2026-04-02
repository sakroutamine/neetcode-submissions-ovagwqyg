# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dep(rt):
            maxd = 0
            if not rt:
                return 0
            if rt.left and rt.right:
                return max(dep(rt.left), dep(rt.right)) +1
            elif rt.left:
                return dep(rt.left) + 1
            elif rt.right:
                return dep(rt.right)+1
            
            return 1

        return dep(root)