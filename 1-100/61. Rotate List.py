#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-20 下午4:13
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        双指针法
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k < 1 or not head:
            return head

        # 获取链表的长度
        link_len = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            link_len += 1

        # 如果 k > link_len,注意去掉重复的循环
        k = k % link_len
        if k == 0:
            return head

        rotate_point = head
        i = 1
        while i < (link_len - k):
            rotate_point = rotate_point.next
            i += 1

        result_head = rotate_point.next
        rotate_point.next = None

        tmp = result_head
        while tmp.next:
            tmp = tmp.next
        tmp.next = head

        return result_head
