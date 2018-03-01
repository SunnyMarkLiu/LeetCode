#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-2-28 下午4:46
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 分两个分支，一个统计奇数节点一个统计偶数节点，最后合并奇数的尾节点和偶数的头节点
        if head is None:
            return None

        result_head = head
        odd_cur = head
        even_head = even_cur = head.next

        while even_cur is not None and even_cur.next is not None:
            tmp = odd_cur.next
            odd_cur.next = odd_cur.next.next
            if odd_cur.next is not None:
                odd_cur = odd_cur.next

            even_cur = tmp
            if even_cur.next is not None:
                even_cur.next = even_cur.next.next

        odd_cur.next = even_head

        return result_head

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 分两个分支，一个统计奇数节点一个统计偶数节点，最后合并奇数的尾节点和偶数的头节点
        if head is None:
            return None

        result_head = head
        odd_cur = head
        even_head = even_cur = head.next

        while even_cur is not None and even_cur.next is not None:
            odd_cur.next = odd_cur.next.next
            even_cur.next = even_cur.next.next
            odd_cur = odd_cur.next
            even_cur = even_cur.next

        odd_cur.next = even_head

        return result_head
