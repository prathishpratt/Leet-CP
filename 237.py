class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

### If you want to optimise the space then delete that orphan node
class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        temp = node.next
        node.next = node.next.next
        del temp    