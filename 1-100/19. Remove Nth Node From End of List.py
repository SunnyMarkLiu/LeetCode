#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-1 下午2:52
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        双指针法：第一个指针先走 n 步，之后两个指针同时走（第二个指针从 head　出发），
        第一个指针到达尾部时，第二个指针所指的节点的　next 就是所要删除的节点

        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first = head

        # first　先走 n 步
        i = 0
        while i < n and first is not None:
            first = first.next
            i += 1

        if first is None:  # 第一个指针走到尾部，说明要移动的节点是头节点
            tmp = head
            head = head.next
            # 删除原头节点
            del tmp
        else:  # 要删除的节点是中间的节点
            # first, second同时出发
            second = head
            while first.next is not None:
                first = first.next
                second = second.next

            # second 的 next　指向的节点就是需要删除的节点
            tmp = second.next
            second.next = second.next.next
            del tmp

        return head
