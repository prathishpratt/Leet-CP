# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        tortoise = head
        hare = head
        flag = 0

        while(hare and hare.next):
            hare = hare.next.next
            tortoise = tortoise.next
            if (hare == tortoise):
                flag = 1
                break
        
        if flag == 0:
            return None

        tortoise = head
        while(hare != tortoise):
            hare = hare.next
            tortoise = tortoise.next

        return tortoise