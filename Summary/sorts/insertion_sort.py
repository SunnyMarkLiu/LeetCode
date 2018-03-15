#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
插入排序
每一步将一个待排序的记录，插入到前面已经排好序的有序序列中去，直到插完所有元素为止。

@author: SunnyMarkLiu
@time  : 18-3-15 下午9:08
"""


def insertion_sort(nums):
    if not nums or len(nums) <= 1:
        return nums

    for i in range(1, len(nums)):  # 从第一个数开始到 len - 1，默认第一个数为有序的
        j = i
        while j > 0 and nums[j] < nums[j - 1]:  # 当前的数比前面排序好的数要小，交换
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1

    return nums


print(insertion_sort([5, 2, 45, 6, 8, 2, 1]))
