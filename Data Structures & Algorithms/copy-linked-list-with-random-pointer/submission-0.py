"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # 第一遍:只复制 val,建立 旧节点→新节点 的映射
        old_to_new = {}
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next
        
        # 第二遍:用映射设置 next 和 random
        cur = head
        while cur:
            old_to_new[cur].next   = old_to_new.get(cur.next)
            old_to_new[cur].random = old_to_new.get(cur.random)
            cur = cur.next
        
        return old_to_new[head]