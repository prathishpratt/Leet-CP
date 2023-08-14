# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Hare and Tortoise
        hare = head
        tortoise = head
        while(hare and hare.next and hare.next.next):
            hare = hare.next.next
            tortoise = tortoise.next

        if (hare.next):
            return tortoise.next
        else:
            return tortoise

        #Using a hash(extra space) 
        # ret = []
        # while(head):
        #     ret.append(head)
        #     head = head.next

        # n =len(ret)
        # if n%2 != 0:
        #     return ret[int((n-1)/2)]
        # else:
        #     return ret[int(n/2)]