#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-4 上午11:27
"""


class Solution(object):
    def maxArea(self, height):
        """
        假设有左指针left和右指针right，且left指向的值小于right的值，假如我们将右指针左移，则右指针左移后的值和左指针指向的值相比有三种情况
        1. 右指针指向的值大于左指针
            这种情况下，容器的高取决于左指针，但是底变短了，所以容器盛水量一定变小
        2. 右指针指向的值等于左指针
            这种情况下，容器的高取决于左指针，但是底变短了，所以容器盛水量一定变小
        3. 右指针指向的值小于左指针
            这种情况下，容器的高取决于右指针，但是右指针小于左指针，且底也变短了，所以容量盛水量一定变小了
        综上所述，容器高度较大的一侧的移动只会造成容器盛水量减小 ，所以应当移动高度较小一侧的指针，并继续遍历，直至两指针相遇。
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1

        max_area = 0
        while left < right:
            # 使用内置的　min max　函数较慢
            if height[left] < height[right]:
                area = height[left] * (right - left)
            else:
                area = height[right] * (right - left)

            if max_area < area:
                max_area = area

            if height[left] < height[right]:  # 左边的值较小
                left += 1
            else:
                right -= 1

        return max_area
