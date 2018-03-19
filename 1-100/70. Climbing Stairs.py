#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-18 下午10:00
"""


class Solution:
    def climbStairs1(self, n):
        """
        方法一，采用递归的方式，注意存在重复计算，用cache缓存计算结果
        :type n: int
        :rtype: int
        """
        return self.climbStairsHelper(n, {})

    def climbStairsHelper(self, n, cache):
        if n == 1:
            return 1

        if n == 2:
            return 2

        if n in cache:
            return cache[n]

        # 此处存在重复计算
        result = self.climbStairsHelper(n - 1, cache) + self.climbStairsHelper(n - 2, cache)
        cache[n] = result

        return result

    def climbStairs(self, n):
        """
        方法二，动态规划，利用状态转移方程 setps(n) = steps(n-1) + steps(n-2)
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1

        steps = [1, 1]

        for i in range(2, n + 1):
            steps.append(steps[-1] + steps[-2])

        return steps[-1]
