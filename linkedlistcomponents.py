# Problem 817

# Attempt with collections.counter, next

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        self.connected = False
        self.count =0 
        self.traverseList(head, G)
        return self.count
    
    def traverseList(self, node, G):
        if node:
            if node.val in G:
                if self.connected == False:
                    self.connected = True
            else:
                if self.connected == True:
                    self.count += 1
                self.connected = False
            self.traverseList(node.next, G)
        else:
            if self.connected == True:
                self.count += 1