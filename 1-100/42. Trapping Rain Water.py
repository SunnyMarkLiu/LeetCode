#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-4 上午11:59
"""


class Solution(object):
    def trap(self, height):
        """
        使用两个指针，一个从左向右遍历，一个从右向左遍历。从左向右遍历时，记录下上次左边的峰值，
        如果右边一直没有比这个峰值高的，就加上这些差值。从右向左遍历时，记录下上次右边的峰值，
        如果左边一直没有比这个峰值高的，就加上这些差值。难点在于，当两个指针遍历到相邻的峰时，
        我们要选取较小的那个峰值来计算差值。所以统一下，我们在遍历左指针或者右指针之前，要先
        判断左右两个峰值的大小。

        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0

        left, right = 0, len(height) - 1
        w_sum = 0

        # 找到左边的第一个峰值
        while left < right and height[left] <= height[left + 1]:
            left += 1

        while left < right and height[right] <= height[right - 1]:
            right -= 1

        # 移动左右指针
        while left < right:
            # 记录左右峰值
            left_peak = height[left]
            right_peak = height[right]

            # 如果左边的峰值小于右边，从左边开始计算
            if left_peak < right_peak:
                left += 1
                while left < right and left_peak >= height[left]:
                    w_sum += left_peak - height[left]
                    left += 1
            else:
                right -= 1
                while left < right and right_peak >= height[right]:
                    w_sum += right_peak - height[right]
                    right -= 1

        return w_sum
