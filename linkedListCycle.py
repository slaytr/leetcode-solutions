# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        self.ans = False
        self.move(head)

        if self.ans:
            return True
        return False
        
    def move(self, node):
        if node:
            print(node.val)
            if node.val != "seen":
                node.val = "seen"
                self.move(node.next)
                
            else:
                self.ans = True