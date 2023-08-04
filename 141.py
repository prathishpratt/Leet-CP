class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #O(n) and O(1) solution
        #Floyd's rabbit and hare algorithm

        slow = head
        fast = head

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False
        # O(n) and O(n) solution 
        # ded = {}
        # temp = head
        # while(temp):
        #     if temp in ded.keys():
        #         return True
        #     else:
        #         ded[temp] = -999
        #     temp = temp.next
        # return False