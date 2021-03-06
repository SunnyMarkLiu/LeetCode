#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
注意判断 l1 和 l2 是否为空以及判断进位是否为空, 可以同时判断处理

@author: MarkLiu
@time  : 17-12-3 下午4:51
"""


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
        carry = 0
        head = n = ListNode(0)
        # 处理非空的 l1 或 l2 或存在的进位 carry
        while l1 or l2 or carry:
            v1, v2 = 0, 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next

            s = v1 + v2 + carry
            carry = s // 10
            val = s % 10
            n.next = ListNode(val)
            n = n.next

        return head.next
