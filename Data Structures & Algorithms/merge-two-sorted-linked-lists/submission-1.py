# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a,b = list1,list2
        dummy = ListNode()
        node = dummy

        while a and b:
            if a.val<=b.val:
                node.next = a
                a=a.next
            else:
                node.next = b
                b=b.next
            node=node.next
        
        if a:
            node.next = a
        elif b:
            node.next = b
        
        return dummy.next