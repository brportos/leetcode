from typing import Optional


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lst1 = 0
        for digit in range(len(l1)):
            num1 = lst1 * 10 + digit
            lst2 = 0
            for digit in range(len(l2)):
                num2 = lst2 * 10 + digit
                result = num1 + num2
                print(result)
if __name__ == "__main__":
    add = Solution()
    add.addTwoNumbers([2, 4, 3], [0,0,0])