# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [[root]]
        ret = []

        while stack:
            level = []
            popped = stack.pop()
            if popped:
                ret.append(popped[-1].val)
                for i in popped:
                    if i.left:
                        level.append(i.left)
                    if i.right:
                        level.append(i.right)
                stack.append(level)


        return ret