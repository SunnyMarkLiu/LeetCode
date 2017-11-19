#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
算法有以下几种：
1、遍历整个链表，将链表每个节点的值记录在数组中，再判断数组是不是一个回文数组，时间复杂度为O（n），但空间复杂度也为O（n），不满足空间复杂度要求。
2、利用栈先进后出的性质，将链表前半段压入栈中，再逐个弹出与链表后半段比较。时间复杂度O（n），但仍然需要n/2的栈空间，空间复杂度为O（n）。
3、**反转链表法**，将链表后半段原地翻转，再将前半段、后半段依次比较，判断是否相等，时间复杂度O（n），空间复杂度为O（1）满足题目要求。

@author: MarkLiu
@time  : 17-11-15 下午8:21
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        previou = None
        current = head
        while current:
            tmp_next = current.next  # 临时保存当前节点的下一个节点, 用于循环后移
            current.next = previou  # 当前节点的下一个节点的指针指向前一个节点, 实现反转
            previou = current  # 和后面一句实现双指针后移
            current = tmp_next
        return previou

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        # 1. 首先需要找到链表的中点，这个可以用快慢指针来实现
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # 此时, fast到达链表的最后一个节点或倒数第二个节点, slow 指向中间的节点(链表奇数个节点)或指向前段的最后一个节点
        # slow 指向的下一个节点是后半段的第一个节点

        # 2. 后半段链表进行反转,获取反转之后的头节点
        reversed_last_half_head = self.reverseList(slow.next)

        # 3. 检查反转之后的链表与前半段是否都相等
        p1, p2 = reversed_last_half_head, head
        while p1 and p2.val == p1.val:  # 遍历后半段, 判断值是否相等
            p1, p2 = p1.next, p2.next

        return p1 is None   # 如果循环结束 p1 为 None, 说明后半段循环结束了, 返回 True
