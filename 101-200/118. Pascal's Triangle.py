#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-2-28 下午7:23
"""


class Solution:
    def generate2(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1], [1, 1]]
        if numRows == 0:
            return []
        if numRows == 1:
            return [result[0]]
        if numRows == 2:
            return result

        for i in range(2, numRows):  # 第i层
            row = []
            for j in range(i - 1):
                row.append(result[i - 1][j] + result[i - 1][j + 1])
            result.append([1] + row + [1])

        return result

    def generate(self, numRows):
        """
        直接解法
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []

        for i in range(numRows):
            result.append([1] * (i + 1))
            if i > 1:
                for j in range(1, i):
                    result[i][j] = result[i - 1][j - 1] + result[i - 1][j]

        return result
