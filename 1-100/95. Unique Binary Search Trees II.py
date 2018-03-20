#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-20 上午10:23
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        1. 每一次都在一个范围内随机选取一个结点作为根。
        2. 每选取一个结点作为根，就把树切分成左右两个子树，直至该结点左右子树为空。

        大致思路如上，可以看出这也是一个可以划分成子问题求解的题目，所以考点是动态规划。
        但具体对于本题来说，采取的是自底向上的求解过程。
        1. 选出根结点后应该先分别求解该根的左右子树集合，也就是根的左子树有若干种，它们组成左子树集合，根的右子树有若干种，它们组成右子树集合。
        2. 然后将左右子树相互配对，每一个左子树都与所有右子树匹配，每一个右子树都与所有的左子树匹配。然后将两个子树插在根结点上。
        3. 最后，把根结点放入链表中。

        :type n: int
        :rtype: List[TreeNode]
        """
        if n < 1:
            return []

        return self.helper(1, n)

    def helper(self, start, end):
        res = []

        # 边界条件
        if start > end:
            res.append(None)
            return res

        for i in range(start, end + 1):  # 当前i作为根结点
            # 小于i构造左子树(list集合)
            left_subtrees = self.helper(start, i - 1)
            # 大于i构造右子树(list集合)
            right_subtrees = self.helper(i + 1, end)

            # 左右结点相互配对组合
            for left_root in left_subtrees:
                for right_root in right_subtrees:
                    # 组合
                    root = TreeNode(i)
                    root.left = left_root
                    root.right = right_root
                    res.append(root)

        return res
