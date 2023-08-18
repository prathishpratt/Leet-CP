# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        while(head and head.val == val):
            head = head.next
        
        prev = head
        i = head
        while(i):
            if i.val == val:
                nxt = i.next
                prev.next = nxt
            else:
                prev = i
            i = i.next

        return head 