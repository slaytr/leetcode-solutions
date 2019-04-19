#Problem 2

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_str = ""
        l2_str = ""
        
        while True:
            if l1 != None:
                l1_str = str(l1.val) + l1_str
                l1 = l1.next
            if l2 != None:
                l2_str = str(l2.val) + l2_str
                l2 = l2.next
            if l1 == None and l2 == None:
                break
                
        l3_str = str(int(l1_str) + int(l2_str))

        objs = [ListNode(l3_str[i]) for i in range(len(l3_str))]
        count = 0
        for obj in objs:
            if count == 0:
                count +=1
                next_obj = obj
                continue
            obj.next = next_obj
            next_obj = obj
        return obj