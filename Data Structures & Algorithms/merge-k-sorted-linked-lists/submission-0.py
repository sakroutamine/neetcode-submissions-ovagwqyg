# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) ==0:
            return None

        def mergeLists(a, b):
            dummy=ListNode()
            node = dummy
            while a and b:
                if a.val<=b.val:
                    node.next = a
                    a=a.next
                else:
                    node.next=b
                    b=b.next
                node=node.next
            if a:
                node.next = a
            elif b:
                node.next = b
            
            return dummy.next
        
        while len(lists)>1:
            level = []
            for i in range(0,len(lists), 2):
                a = lists[i]
                b = lists[i+1] if (i+1<len(lists)) else None

                level.append(mergeLists(a,b))

            lists = level
        return lists[0]

