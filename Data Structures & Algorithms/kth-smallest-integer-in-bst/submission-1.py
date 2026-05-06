# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []
        if not root:
            return -1

        def order(node):
            nonlocal inorder
            if not node:
                return

            order(node.left)
            inorder.append(node.val)
            order(node.right)

            return

        order(root)
        return inorder[k-1]

        

