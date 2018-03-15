#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
希尔排序
希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，
整个文件恰被分成一组，算法便终止。

@author: SunnyMarkLiu
@time  : 18-3-15 下午9:24
"""


def shell_sort(nums):
    if not nums or len(nums) <= 1:
        return nums

    # 增量gap，并逐步缩小增量
    gap = len(nums) // 2
    while gap > 0:
        # 从第gap个元素，逐个对其所在组进行直接插入排序操作
        for i in range(gap, len(nums)):
            j = i

            while j - gap >= 0 and nums[j] < nums[j - gap]:
                nums[j], nums[j - gap] = nums[j - gap], nums[j]
                j -= gap

        gap = gap // 2

    return nums


print(shell_sort([5, 2, 45, 6, 8, 2, 1]))
