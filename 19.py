# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #creat a dummy node at front
        dummy = ListNode(next=head)

        left = dummy
        right = head

        while(n>0):
            right = right.next
            n -=1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next          #dont return head

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
