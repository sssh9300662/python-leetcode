class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        vals = []
        result = None
        
        while l1:
            vals.append(l1.val)
            l1 = l1.next
        while l2:
            vals.append(l2.val)
            l2 = l2.next
        
        vals.sort()
        current = None
            
        for val in vals:
            if not current:
                result = ListNode(val)
                current = result
            else:
                node = ListNode(val)
                current.next = node
                current = node
                
        return result


if __name__ == "__main__":
    l1 = ListNode(1)
    l11 = ListNode(2)
    l12 = ListNode(4)

    l11.next = l12
    l1.next = l11
    
    l2 = ListNode(1)
    l21 = ListNode(3)
    l22 = ListNode(4)
    
    l21.next = l22
    l2.next = l21
    
    s = Solution()
    print(s.mergeTwoLists(l1, l2))