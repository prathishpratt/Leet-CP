# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        #Optimal
        #Idea: Let both pointer run to end and when one reached end, put that as the
        #start of other list. So after both reaching the end once, both will
        #again meet at the itersection. Its not intuituve so mug. 

        ha = headA
        hb = headB

        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        
        return ha


        #Naive
        # k = []

        # while(headA):
        #     k += [headA]
        #     headA = headA.next
        
        # while(headB):
        #     if headB in k:
        #         return headB
        #     headB = headB.next
        # return None