#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
2 的倍数:
1  1 <-
2  10
4  100 <-
8  1000
16 10000 <-
...

4 的倍数:
1  1
4  100
16 10000
64 1000000

因此, 4的幂就是2的幂过滤掉 2, 8 的这类情况
5(0101) & 2(0010) = 0000
5(0101) & 4(0100) = 0100
5(0101) & 8(1000) = 0000


若一个整数是4的幂，则其二进制形式具有如下特点：

1. 最高位为1，其余位为0
2. 0的个数为偶数

条件1可以用 num & (num - 1) == 0 判断
条件2可以用 num & 0x55555555 > 0 判断

@author: MarkLiu
@time  : 17-12-6 下午8:42
"""


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and num & (num - 1) == 0 and (num & 0x55555555) > 0
