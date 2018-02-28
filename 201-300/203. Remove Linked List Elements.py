#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-2-28 下午3:25
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements2(self, head, val):
        """
        双指针法
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 首先找到 head 节点
        while head is not None and head.val == val:
            head = head.next
        result_head = head

        if result_head is None:
            return None

        # 采用双指针的方法
        current_tmp_head = result_head
        current_end_pointer = result_head.next
        while current_end_pointer is not None:

            # 相等，while 循环去除 val 节点
            while current_end_pointer.val == val:
                current_tmp_head.next = current_end_pointer.next
                current_end_pointer = current_end_pointer.next
                if current_end_pointer is None:
                    break

            if current_end_pointer is None:
                break

            # 不相等，头指针和末尾指针后移1位
            current_tmp_head = current_end_pointer
            current_end_pointer = current_end_pointer.next

        return result_head

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 首先找到 head 节点
        while head is not None and head.val == val:
            head = head.next
        result_head = head

        if result_head is None:
            return None

        current = result_head
        while current is not None:
            while current.next is not None and current.next.val == val:
                current.next = current.next.next

            current = current.next

        return result_head
