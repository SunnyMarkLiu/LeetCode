#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
简单选择排序
每一趟从待排序的数据元素中选择最小（或最大）的一个元素作为首元素，直到所有元素排完为止

@author: SunnyMarkLiu
@time  : 18-3-15 下午8:27
"""


def simple_select_sort(nums):
    if not nums or len(nums) <= 1:
        return nums

    for i in range(len(nums) - 1):
        min_index = i  # 记录最小值的下标

        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j

        if min_index != i:
            nums[min_index], nums[i] = nums[i], nums[min_index]

    return nums


print(simple_select_sort([5, 2, 45, 6, 8, 2, 1]))
