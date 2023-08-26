# BETTER SOLUTION
# class Solution:
#     def reorderList(self, head):
#         #step 1: find middle
#         if not head: return []
#         slow, fast = head, head
#         while fast.next and fast.next.next:
#             slow = slow.next
#             fast = fast.next.next
        
#         #step 2: reverse second half
#         prev, curr = None, slow.next
#         while curr:
#             nextt = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nextt    
#         slow.next = None
        
#         #step 3: merge lists
#         head1, head2 = head, prev
#         while head2:
#             nextt = head1.next
#             head1.next = head2
#             head1 = head2
#             head2 = nextt

# MU SOLUTION
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = head
        ar = []
        while temp:
            ar.append(temp)
            temp = temp.next

        i, j = 0, len(ar)-1
        while i<j:
            x = ar[i]
            y = ar[j]
            temp = x.next
            x.next = y
            if j != i+1:
                y.next = temp
                ar[j-1].next = None
            else:
                y.next = None
            i = i+1
            j = j-1
        return head
