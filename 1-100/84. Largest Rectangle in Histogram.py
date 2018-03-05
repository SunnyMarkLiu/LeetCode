#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-5 下午5:30
"""


class Solution(object):
    def largestRectangleArea1(self, heights):
        """
        暴力搜索: 对于每个矩形,从左往右遍历计算面积取最大值
        时间复杂度　O(n^2)
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        for i in range(len(heights)):
            min_height = heights[i]

            for j in range(i, -1, -1):
                min_height = min(min_height, heights[j])
                area = min_height * (i - j + 1)
                if area > max_area:
                    max_area = area
        return max_area

    def largestRectangleArea2(self, heights):
        """
        优化暴力搜索: 对于每个矩形,从左往右遍历计算面积取最大值，对于右边比当前还大的，不需要遍历
        只对合适的右边界（峰顶），往左遍历面积
        时间复杂度　O(n^2)
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        for i in range(len(heights)):

            # 此处优化：对于右边比左边的小的，不需要遍历
            if i < len(heights) - 1 and heights[i] <= heights[i + 1]:
                continue

            min_height = heights[i]

            for j in range(i, -1, -1):
                min_height = min(min_height, heights[j])
                area = min_height * (i - j + 1)
                if area > max_area:
                    max_area = area
        return max_area

    def largestRectangleArea(self, heights):
        """
        http://www.cnblogs.com/lichen782/p/leetcode_Largest_Rectangle_in_Histogram.html

        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        max_area = 0
        stack = []
        i = 0

        while i < len(heights):
            # 当前元素大于栈顶元素，stack 中保存递增的下标
            if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            else:
                # 当前元素小于栈顶元素，出栈（下标），计算面积
                top_i = stack.pop()
                if len(stack) == 0:
                    area = heights[top_i] * i
                else:
                    area = heights[top_i] * (i - (stack[-1] + 1))

                max_area = max(max_area, area)

        return max_area
