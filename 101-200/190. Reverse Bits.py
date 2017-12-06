#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
result初始值为0, 依次获取最后一位, 左移一位, 原数据右移一位
注意 result 移动的次数比获取原数据最后一位的次数少一

@author: MarkLiu
@time  : 17-12-6 下午9:19
"""


class Solution(object):
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0

        for i in range(32):
            result += n & 1
            n >>= 1
            # 注意 result 移动的次数比获取原
            if i < 31:
                result <<= 1

        return result
