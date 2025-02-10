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


# Mine - Latest and better
# def reorderList(self, head: Optional[ListNode]) -> None:
#         # First find the middle element
#         # Then Break them as two LL
#         # Then reverse the second part
#         # Then merge them

#         slow = head
#         fast = head.next

#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next

#         temp = slow.next
#         prev = slow.next = None

#         #reverse the LL
#         while temp:
#             nxt = temp.next
#             temp.next = prev
#             prev = temp
#             temp = nxt
        
#         list1 = head
#         list2 = prev

#         #now merge
#         while list1 and list2:
#             nxt1 = list1.next
#             nxt2 = list2.next

#             list1.next = list2
#             list2.next = nxt1
            
#             list1 = nxt1
#             list2 = nxt2
