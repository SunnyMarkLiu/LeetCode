#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-1 下午3:04
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        检测链表是否存在环，并找到环的入口点
        :type head: ListNode
        :rtype: ListNode
        """
        while head is None or head.next is None:
            return None

        fast = head
        slow = head

        # 检测是否存在环
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  # 存在环，fast记录了第一次相遇点
                break

        if fast is None or fast.next is None:  # 不存在环
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
