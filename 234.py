# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #We can do this by hashing and it way easier. 
        #bUT THEY ASKING 0(1) space

        #So find middle by hare and tort, reverse after that and then check

        #Find middle
        hare = head
        tort = head

        while(hare and hare.next):
            hare = hare.next.next
            tort = tort.next
        #Now tort at middle

        #Reverse after tort
        prev = None
        while(tort):
            nxt = tort.next
            tort.next = prev
            prev = tort
            tort = nxt

        #Now prev is the last ele's pointer
        #So wo compare from head and prev and traverse
        while(prev):
            if (prev.val != head.val):
                return False
            prev = prev.next
            head = head.next
        return True