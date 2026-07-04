from typing import Optional


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution():
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()
        carry = 0
        while (l1 != None) or (l2 != None) or (carry != 0):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = val1 + val2
            l1 = l1.next
            l2 = l2.next
        return list(val)
if __name__ == "__main__":
    add = Solution()
    add.addTwoNumbers(['2', '4', '3'], ['5', '6', '4'])