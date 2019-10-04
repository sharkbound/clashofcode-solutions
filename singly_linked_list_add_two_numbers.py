# https://leetcode.com/problems/add-two-numbers/submissions/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        number = self.extract_number(l1) + self.extract_number(l2)

        node = ListNode(None)
        last = None
        root = node
        for digit in map(int, str(number)[::-1]):
            node.val = digit
            node.next = next_node = ListNode(None)
            last = node
            node = next_node
        last.next = None
        return root

    def extract_number(self, node):
        out = []
        while node is not None:
            out.append(node.val)
            node = node.next
        return int(''.join(map(str, out))[::-1])
