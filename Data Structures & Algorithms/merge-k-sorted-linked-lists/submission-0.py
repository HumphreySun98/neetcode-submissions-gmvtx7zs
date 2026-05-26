# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        vals = []
        for head in lists:
            cur = head
            while cur:
                vals.append(cur.val)
                cur = cur.next
        
        vals.sort()
        dummy = ListNode(0)
        cur = dummy
        for v in vals:
            cur.next = ListNode(v)
            cur = cur.next

        return dummy.next




        
        