#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
归并排序
首先归并排序使用了二分法，归根到底的思想还是分而治之。拿到一个长数组，
将其不停的分为左边和右边两份，然后以此递归分下去。然后再将她们按照两个有序数组的样子合并起来

@author: SunnyMarkLiu
@time  : 18-3-15 下午9:50
"""


def merge(left, right):
    """
    合并两个排序好的数组
    """
    result = []
    left_i = right_i = 0

    while left_i < len(left) and right_i < len(right):

        if left[left_i] < right[right_i]:  # 比较 left和right 的大小
            result.append(left[left_i])
            left_i += 1
        else:
            result.append(right[right_i])
            right_i += 1

    # 如果左边有剩余，则直接加入剩下的
    if left_i < len(left):
        result.extend(left[left_i:])

    if right_i < len(right):
        result.extend(right[right_i:])

    return result


def merge_sort(nums):
    if not nums or len(nums) <= 1:
        return nums

    # 分而
    mid = len(nums) // 2

    left_sorted = merge_sort(nums[:mid])
    right_sorted = merge_sort(nums[mid:])

    # 治之
    return merge(left_sorted, right_sorted)


l = [4, 6, 8, 5, 9]
print(l)
l = merge_sort(l)
print(l)
