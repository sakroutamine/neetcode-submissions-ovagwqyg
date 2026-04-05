"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def height(node):
            h=0
            while node:
                h+=1
                node = node.parent
            return h
        
        heightp = height(p)
        heightq = height(q)

        if heightp < heightq:
            p,q = q,p
            heightp, heightq = heightq, heightp

        while heightp > heightq:
            p = p.parent
            heightp -=1
        
        while p!=q:
            p=p.parent
            q=q.parent

        return p


        