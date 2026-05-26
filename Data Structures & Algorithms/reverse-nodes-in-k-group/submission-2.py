# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        count = 0
        while cur and count <k:
            cur = cur.next
            count += 1

        if count < k:
            return head

        new_head = self.reversefirstK(head,k)
        head.next = self.reverseKGroup(cur,k)

        return new_head

        

    


    def reversefirstK(self,head,k):
        prev = None
        cur = head

        for _ in range(k):
            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur =nxt

        return prev