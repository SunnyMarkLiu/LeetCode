#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
快速排序

@author: SunnyMarkLiu
@time  : 18-3-18 下午1:23
"""


def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    # 以最低位为基准数
    key_index = low
    while left < right:
        # 右分支找到小于基准数的下标
        while left < right and array[right] > array[key_index]:
            right -= 1

        # 左分支找到大于基准数的下标
        while left < right and array[left] <= array[key_index]:
            left += 1

        # 找到之后交换
        array[left], array[right] = array[right], array[left]

    # 此时 left == right，交换基准数
    array[left], array[key_index] = array[key_index], array[left]

    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)


def quick_sort_stack(array, l, r):
    if l >= r:
        return
    stack = []
    stack.append(l)
    stack.append(r)
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high - low <= 0:
            continue
        x = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        stack.extend([low, i, i + 2, high])


l = [4, 6, 8, 5, 9]
print(l)
quick_sort_stack(l, 0, len(l) - 1)
print(l)
