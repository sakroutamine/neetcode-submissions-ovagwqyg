# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        a,b = root, root
        top = root
        while a==b:
            # print(a.val, b.val)
            if not a or not b:
                return top
            if a.val > p.val:
                a=a.left
            elif a.val < p.val:
                a=a.right
            if b.val>q.val:
                b=b.left
            elif b.val < q.val:
                b=b.right
            if a and b:
                print(a.val, b.val)
            if a and b and a.val==b.val:
                top = a

        return top