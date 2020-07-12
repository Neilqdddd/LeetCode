# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        answer = ListNode(0)
        temp = answer
        carry = 0
        while l1 or l2 or carry != 0:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, remain = divmod(carry, 10)
            temp.next = ListNode(remain)
            temp = temp.next
        return answer.next


'''
Not perfect.
Runtime: 84 ms, faster than 23.90% of Python online submissions for Add Two Numbers.
Memory Usage: 12.6 MB, less than 93.31% of Python online submissions for Add Two Numbers.
'''


