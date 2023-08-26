# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        while fast and n>0:
            fast = fast.next
            n = n-1
        
        dummy = ListNode(next = head)
        slow = dummy
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

        # temp = head
        # ar = []
        # while temp:
        #     ar.append(temp)
        #     temp = temp.next
        # if len(ar) <=1:
        #     return None    
        # if n == 1:
        #     x = ar[-(n+1)]
        #     x.next = None
        #     return head
        # if n == len(ar):
        #     return head.next
        # try:
        #     ar[-n-1].next = ar[-n+1]
        # except:
        #     pass
        # return head