# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = {}
        temp = head

        if head == None or head.next == None:
            return head

        while(temp):
            if temp.val in s.keys():
                s[temp.val] = 2
            else:
                s[temp.val] = 1
            temp =temp.next
        
        try:
            while (s[head.val] ==2 and head):
                head = head.next
        except:
            return head

        prev = head
        temp = head.next  

        try:
            while(temp):
                while(s[temp.val] == 2):
                    prev.next = temp.next
                    temp = temp.next
                prev = temp
                temp = temp.next
        except:
            return head
        
        return head

        