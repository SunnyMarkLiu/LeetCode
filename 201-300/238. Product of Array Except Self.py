#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-4 下午3:29
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        https://leetcode.com/problems/product-of-array-except-self/discuss/65622/Simple-Java-solution-in-O(n)-without-extra-space/67603

        Numbers:     2    3    4     5
        Lefts:       1    2  2*3 2*3*4
        Rights:  3*4*5  4*5    5     1

        result = Lefts * Rights

        先计算 left，结果保存在 result 中，再计算 right ，循环乘以 result
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [1] * n

        # 先计算 left，结果保存在 result 中
        left = 1
        for i in range(n):
            if i > 0:
                left = left * nums[i - 1]
            result[i] = left
        # print(result)

        # 再计算 right ，循环乘以 result
        right = 1
        for i in range(n - 1, -1, -1):
            if i < n - 1:
                right = right * nums[i + 1]
            result[i] = result[i] * right

        return result
