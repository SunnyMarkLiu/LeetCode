#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-20 下午5:12
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        """
        归并排序的思想
        :type head: ListNode
        :rtype: ListNode
        """
        # 当前结点为None或只有一个结点
        if not head or not head.next:
            return head

        # step 1. cut the list to two halves
        # 找到链表的中点
        fast = slow = head
        pre = slow
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        # 分成两个链表，slow指向中点
        pre.next = None

        # step 2. sort each half
        left_half = self.sortList(head)
        right_half = self.sortList(slow)

        # step 3. merge l1 and l2
        return self.merge(left_half, right_half)

    def merge(self, l1, l2):
        """ 两个链表合并 """
        # 添加临时结点，方便存放头结点
        head = res = ListNode(-1)

        while l1 and l2:
            if l1.val < l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next
            res = res.next

        if l1:
            res.next = l1

        if l2:
            res.next = l2

        return head.next
