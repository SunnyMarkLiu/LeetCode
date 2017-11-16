#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
一个很容易想到的方法是用数组保存新构造每个节点，然后反向构造链表.

iterative: 循环得到下一个节点，更改当前节点指向，将指针往下移动，直到过完整个linkedlist.
@author: MarkLiu
@time  : 17-11-16 下午7:45
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        循环迭代 iterative 的方法, beat 93.28%
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


head_ = ListNode(0)
node1 = ListNode(1)
node2 = ListNode(2)

head_.next = node1
node1.next = node2
result = Solution().reverseList(head_)
while result:
    print result.val
    result = result.next
