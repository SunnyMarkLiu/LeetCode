#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
@author: MarkLiu
@time  : 17-12-4 上午10:49
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        used_set = set()
        r_head = move = ListNode(None)
        while head:
            v = head.val
            if v not in used_set:
                used_set.add(v)
                move.next = head
                move = head
                head = head.next
                continue
            head = head.next
        move.next = None

        return r_head.next

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = head
        while result:
            if result.next is None:
                break

            # 重复数据发生在相邻数字
            if result.val == result.next.val:
                result.next = result.next.next
            else:
                result = result.next

        return head
