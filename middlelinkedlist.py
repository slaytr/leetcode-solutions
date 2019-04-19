#Problem 876 - No recursion - n + n/2, O(n)

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        first = head
        count = 1
        while head.next != None:
            head = head.next
            count +=1
        for i in range(count//2):
            first = first.next
        return first

'''
#Using Hashtable - n + 1, O(n)
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        out = {}
        count = 1
        out[count] = head
        while head.next != None:
            head = head.next
            count +=1
            out[count] = head
        if count == 1:
            return out[1]
        else:
            return out[count//2+1]
'''