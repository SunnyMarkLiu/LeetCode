#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-15 下午7:46
"""


class Solution(object):
    def numTrees(self, n):
        """
        遍历对1-n的每个数 i 作为根结点，小于 i 的作为左子树，大于 i 的作为右子树
        注意：会存在大量的重复计算：1）小于 i 的自然存在重复的 2）大于 i 的其实也存在重复计算，因为顺序和小于i一样的
        1,2,3, 4, i=5, 6,7,8
        计算右边的6,7,8 和计算左边的1,2,3是一样的

        遍历每个数，将当前数作为根结点，左右两边序列构成的数相乘，
        对每个数的结果相加
        :type n: int
        :rtype: int
        """
        res_map = {}
        return self.helper(n, res_map)

    def helper(self, n, res_map):
        if n in res_map:
            return res_map[n]

        if n <= 1:
            res_map[n] = 1
            return 1

        # 递归
        sum = 0
        for i in range(1, n + 1):
            # 以 i 为根结点，计算小于 i 的BST数 × 大于 i 的BST数 ==> i 为根结点的BST数
            sum += self.helper(i - 1, res_map) * self.helper(n - i, res_map)

            # 缓存起来
        res_map[n] = sum
        return sum
