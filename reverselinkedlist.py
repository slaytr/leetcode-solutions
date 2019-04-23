#Problem 206
'''
#recur
class Solution:
    def reverseList(self, head: ListNode, tail=None) -> ListNode:
        head.next, tail, head = tail, head, head.next
        return self.reverseList(head, tail) if head else tail
#iter
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p = None
        while head: head.next, p, head = p, head, head.next
        return p
'''
# mine
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #recur
        if head == None:
            return None
        
        self.new_head = None
        
        def reverse(self, node, prev):
            if node != None:
                reverse(self, node.next, node)
                node.next = prev
            else:
                self.new_head = prev
                
        reverse(self, head.next, head)
        head.next = None
        
        return self.new_head     
    	#iter
        '''
        if head == None:
            return None
        stack = []
        while head != None:
            stack.append(head)
            head = head.next
        for i in range(len(stack)):
            if i == len(stack)-1:
                stack[(len(stack)-1)-i].next = None
            else:
                stack[(len(stack)-1)-i].next = stack[(len(stack)-1)-(i+1)]
        return stack[len(stack)-1]
        '''