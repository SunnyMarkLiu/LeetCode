#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
冒泡排序
@author: SunnyMarkLiu
@time  : 18-3-15 下午8:03
"""


def bubble_sort(nums):
    if not nums or len(nums) <= 1:
        return nums

    for i in range(len(nums) - 1):  # 外轮循环从 0 到 len(nums) - 1
        has_sorted = True   # 记录剩下的是否为有序，如果有序直接 break

        for j in range(len(nums) - i - 1):  # 外轮循环从 0 到已经处理过倒数 i 个的位置
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                has_sorted = False

        if has_sorted:
            break

    return nums


print(bubble_sort([5, 2, 45, 6, 8, 2, 1]))
