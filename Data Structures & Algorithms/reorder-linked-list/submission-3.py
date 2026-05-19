# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None

        prev = None
        cur = second

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        first = head
        second = prev

        while second:
            tem1 = first.next
            tem2 = second.next

            first.next = second
            second.next = tem1

            first = tem1
            second = tem2

            

        