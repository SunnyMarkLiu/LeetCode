#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
@author: MarkLiu
@time  : 17-11-21 下午8:54
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        res = ListNode(0)
        head = res

        while l1 and l2:
            if l1.val > l2.val:
                res.next = l2
                l2 = l2.next
            else:
                res.next = l1
                l1 = l1.next
            res = res.next

        if l1:
            res.next = l1
        if l2:
            res.next = l2

        return head.next
