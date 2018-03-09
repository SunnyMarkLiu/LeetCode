#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
根节点应该是有序链表的中间点，从中间点分开为左右两个有序链表，在分别找出其中间点作为原中间点的左右两个子节点，
这不就是是二分查找法的核心思想么。所以这道题考的就是二分查找法

@author: SunnyMarkLiu
@time  : 18-3-9 下午1:36
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST１(self, head):
        """
        缺点是修改了链表的结构，因为载在找到中间的点后，将前面的点的 next 设置为了 None
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None

        return self.dfs(head)

    def dfs(self, head):
        if not head:
            return None

        # 当前结点为最后一个结点，则直接创建 TreeNode返回
        if not head.next:
            return TreeNode(head.val)

        # 快慢指针获取中间结点
        slow = fast = head
        tmp = head
        while fast and fast.next:
            tmp = slow
            slow = slow.next
            fast = fast.next.next

        # 此时 slow 指向链表的中间节点
        node = TreeNode(slow.val)
        tmp.next = None

        # 创建左右子树
        node.left = self.dfs(head)
        node.right = self.dfs(slow.next)
        return node

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None

        return self.dfs2(start=head, end=None)

    def dfs2(self, start, end):

        if not start:
            return None

        # start 和 end 相等，说明指向已经处理过的结点了（上一次的中点）或者链表的尾部
        if start == end:
            return None

        slow = fast = start
        while fast != end and fast.next != end:
            slow = slow.next
            fast = fast.next.next

        # 此时 slow 指向链表的中间节点
        node = TreeNode(slow.val)
        # 创建左右子树
        node.left = self.dfs2(start, slow)  # 注意是左闭右开区间，构建左子树时 end 应为刚刚处理过的中间结点 slow
        node.right = self.dfs2(slow.next, end)

        return node

