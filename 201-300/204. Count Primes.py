#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-6 下午1:17
"""


class Solution(object):
    def countPrimes(self, n):
        """
        计算小于非负数 n 的质数的数目
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        # 标记小于 n 的所有数是否是质数，初始化全标记为 1，全是质数
        prime = [0, 0] + [1] * (n - 2)

        # 不用遍历到 n,　边界值遍历到　sqrt(n) ^ 2 = n
        for i in range(2, int(n ** 0.5) + 1):
            # 如果当前 i 是质数，则对应的倍数将不是质数
            if prime[i] == 1:
                j = 2
                while i * j < n:
                    prime[i * j] = 0
                    j += 1

        count = sum(prime)
        return count
