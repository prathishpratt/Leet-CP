# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        cur = dummy

        while(l1 or l2 or carry):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0 

            val = val1 + val2 + carry
            carry = val//10
            val = val%10

            cur.next = ListNode(val)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next

        return dummy.next

        #Naive Solution
        # count = 0
        # temp, num1 = l1, ""
        # ret, num2 = l2,""
        # while(temp):
        #     num1 = num1+str(temp.val)
        #     temp = temp.next
        # while(ret):
        #     num2 = num2+str(ret.val)
        #     ret = ret.next

        # num1 = int(num1[::-1])
        # num2 = int(num2[::-1])

        # num = str(num1+num2)
        # num = num[::-1]
        # temp=l1

        # for i in range(0,len(num)):
        #     temp.val = num[i]
        #     if temp.next == None and i != len(num)-1:
        #         temp.next = ListNode()
        #     temp = temp.next
        # return l1
            