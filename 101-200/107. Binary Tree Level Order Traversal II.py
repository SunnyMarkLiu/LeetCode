#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-8 下午2:37
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom1(self, root):
        """
        方法1：递归
        和自顶向下的层次遍历类似，只不过再存储每层的数据的方式有所改变，自底向上是从 [] 的头部插入就 ok 了
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result

        self.levelOrderBottomHelper(root, result, 0)
        return result

    def levelOrderBottomHelper(self, root, result, level):
        if not root:
            return

        if level == len(result):    # 遍历新的当前层
            current = [root.val]
            result.insert(0, current)   # 注意从头部插入
        else:  # level < len(result)，遍历到前面的 level
            level_result = result[-(level + 1)]
            level_result.append(root.val)
            result[-(level + 1)] = level_result

        self.levelOrderBottomHelper(root.left, result, level + 1)
        self.levelOrderBottomHelper(root.right, result, level + 1)

    def levelOrderBottom(self, root):
        """
        方法2：迭代
        和自顶向下的层次遍历类似，只不过再存储每层的数据的方式有所改变，自底向上是从 [] 的头部插入就 ok 了
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result

        current_level = [root]
        while current_level:
            cur_level_res = []
            next_level_nodes = []

            for node in current_level:
                cur_level_res.append(node.val)
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)

            result.insert(0, cur_level_res)
            current_level = next_level_nodes

        return result
