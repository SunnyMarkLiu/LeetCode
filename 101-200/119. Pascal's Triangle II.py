#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-2-28 下午7:25
"""


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]

        # 先开辟这样大小的数组
        result = [1] * (rowIndex + 1)

        # 分别计算每个层
        for i in range(rowIndex + 1):
            if i > 1:
                # 从后往前分别计算每个元素的值
                for j in range(i - 1, 0, -1):
                    result[j] = result[j - 1] + result[j]

        return result
