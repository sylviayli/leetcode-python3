# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, add_next=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == 0:
            l1 = ListNode(0)
        if l2 == 0:
            l2 = ListNode(0)
        first = l1.val
        second = l2.val
        result = ListNode((first + second + add_next) % 10)
        add_next = (first + second + add_next) // 10
        if l1.next and l2.next:
            result.next = self.addTwoNumbers(l1.next, l2.next, add_next)
        elif not l1.next and l2.next:
            result.next = self.addTwoNumbers(0, l2.next, add_next)
        elif l1.next and not l2.next:
            result.next = self.addTwoNumbers(l1.next, 0, add_next)
        elif not l1.next and not l2.next and add_next:
            result.next = self.addTwoNumbers(0, 0, add_next)

        return result
