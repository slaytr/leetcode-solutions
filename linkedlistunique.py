#Problem 83 Remove Duplicates from Sorted List 99.96% speed
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head:
            self.prev = head
            self.trav(head.next)
            return head
    
    def trav(self, node):
        if node:
            if self.prev.val == node.val:
                self.prev.next = node.next
            else:
                self.prev = node
            self.trav(node.next)