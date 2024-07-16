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
        dummy = Node(0)
        prev = dummy
        temp = head
        has = {}
        
        while(temp):
            k = Node(temp.val,None, None)
            prev.next = k
            has[temp] = k
            prev = prev.next
            temp = temp.next
            
        temp = dummy.next
        j = head
        while(j):
            if j.random == None:
                temp.random = None
            else:
                temp.random = has[j.random]
            temp = temp.next
            j = j.next
        return dummy.next
