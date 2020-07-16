# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# not really understand
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return head

        temp, dummy, count = head, None, 0

        while temp.next is not None:
            temp = temp.next
            count += 1
            if count == n:
                dummy = head
            if dummy and count != n:
                dummy = dummy.next

        if dummy is None:
            head = head.next
        else:
            dummy.next = dummy.next.next

        return head


'''
Runtime: 24 ms, faster than 61.37% of Python online submissions for Remove Nth Node From End of List.
Memory Usage: 12.9 MB, less than 12.03% of Python online submissions for Remove Nth Node From End of List.
'''
