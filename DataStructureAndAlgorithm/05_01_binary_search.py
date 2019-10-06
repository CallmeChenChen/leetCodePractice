# -*- coding: utf-8 -*-
# @Author : zhaochen
# @Date   : 2019/10/4
# @File   : 05_01_binary_search.py

"""二分查找联系题"""

# 找到目标值的第一个位置
def search_value_first(nums, val):
    if not nums:
        return -1
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == val:
            while nums[mid] == val:
                mid = mid - 1
            return mid + 1
        elif nums[mid] > val:
            right = mid -1
        else:
            left = mid + 1
    return -1

search_value_first([1,1,1,2,2,2,3,3,3,4],0)


def search_value_first1(nums, val):
    if not nums:
        return []
    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] == val:
            right = mid
        elif nums[mid] < val:
            left = mid
        else:
            right = mid
    if nums[left] == val:
        return left
    if nums[right] == val:
        return right
    return -1
search_value_first1([1,1,1,2,2,2,3,3,3,4],2)
# 找到目标值的最后一个位置
def search_value_last(nums, val):
    if not nums:
        return -1
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == val:
            while nums[mid] == val:
                mid = mid + 1
            return mid - 1
        elif nums[mid] > val:
            right = mid -1
        else:
            left = mid + 1
    return -1

search_value_last([1,1,1,2,2,2,3,3,3,4],1)

def search_value_last1(nums, val):
    if not nums:
        return []
    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] == val:
            left = mid
        elif nums[mid] < val:
            left = mid
        else:
            right = mid
    print(nums[left], nums[right])
    if nums[right] == val:
        return right
    if nums[left] == val:
        return left
    return -1
search_value_last1([1,2,2,3],2)
# 旋转有序数组找最小值
# 要想清楚什么是旋转数组
def rotated_list_min(nums):
    if not nums:
        return -1
    left, right = 0, len(nums) - 1
    while left + 1 < right:
        if nums[left] < nums[right]:
            return nums[left]
        mid = left + (right - left) // 2
        if nums[mid] > nums[left]:
            left = mid
        else:
            right = mid
    return nums[left] if nums[left] < nums[right] else nums[right]
rotated_list_min([7,6])

# 旋转数组 查值
def rotated_list(nums, val):
    if not nums:
        return -1
    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] == val:
            return mid
        if nums[mid] > nums[left]:
            if nums[mid] >= val and nums[left] <= val:
                right = mid
            else:
                left = mid
        else:
            if nums[mid] <= val and nums[right] >= val:
                left = mid
            else:
                right = mid
    if nums[left] == val:
        return left
    if nums[right] == val:
        return right
    return -1

rotated_list([4,5,6,1,2,3],1)

# 搜索插入位置 假设数组中不存在重复数 类似bisect
def search_insert_pos(nums, val):
    if not nums:
        return []
    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] == val:
            return mid
        if nums[mid] > val:
            right = mid
        else:
            left = mid

    if nums[left] >= val:
        return left
    if nums[right] >= val:
        return right

    return right+1

search_insert_pos([1,3,4,7,8,10],-1)

# 搜索一个区间， 目标值开始位置和结束位置
def search_val_interval(nums, val):
    if not nums:
        return []
    # 先找第一个位置
    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] == val:
            right = mid
        elif nums[mid] > val:
            right = mid
        else:
            left = mid
    if nums[left] == val:
        lbound = left
    elif nums[right] == val:
        lbound = right
    else:
        return -1,-1
    # 再找最后一个位置
    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] == val:
            left = mid
        elif nums[mid] > val:
            right = mid
        else:
            left = mid
    if nums[left] == val:
        rbound = left
    elif nums[right] == val:
        rbound = right
    else:
        return -1, -1

    return lbound, rbound

search_val_interval([1,1,2,2,2,3,3,4,5], 3)

# 在用空字符串隔开的字符串有序列中查找
def search_chars_val(nums, val):
    if not nums:
        return []
    left, right = 0, len(nums) -1
    while left + 1 < right:
        while nums[left] == '' and left + 1 < right:
            left += 1
        if nums[left + 1] == '':
            left = left + 1
        if left+1 >= right:
            return -1

        mid = left + (right - left) // 2
        while nums[mid] == '':
            mid +=1
        if nums[mid] == val:
            return mid
        elif nums[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    if nums[left] == val:
        return left
    if nums[right] == val:
        return right
    return -1
search_chars_val(['','','',1,2,2,2,'','',2,3],2)
search_chars_val([''],2)
# 在无线序列中找到某元素的第一个出现的位置
# 倍增法 + 二分查找


def infinite_sequence_first(nums, val):
    if not nums:
        return []
    left, right = 0, 1
    while nums[right] < val:
        left = right
        right = 2 * right
        if len(nums) <= right:
            right = len(nums) - 1
            break

    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] == val:
            return mid
        elif nums[mid] > val:
            right = mid
        else:
            left = mid
    if nums[right] == val:
        return right
    if nums[left] == val:
        return left
    return -1

infinite_sequence_first([1,2,3,4,5,6,7,8,9,10,15,19,20,25,27,29],29)

# 供暖设备
from bisect import bisect
bisect([1,3,4,5,6,9],2)
def heaters(houses, heaters):
    pass

# 开平方
def sqrt_(x):
    if x == 0:
        return 0
    if x < 0:
        return None
    left, right = 1, x
    while left <= right:
        mid = left + (right - left) // 2
        if mid == x // mid:
            return mid
        elif mid < x // mid:
            left = mid + 1
        else:
            right = mid - 1
    return right

sqrt_(9)

def newton_sqrt(x):
    r = x
    while r * r > x:
        r = (r + x // r) // 2
    return r

newton_sqrt(10)

# 矩阵搜索 N*M的有序矩阵中查值
# 矩阵搜索 N*M的有序矩阵中找第k大数值

# 找重复数
def find_duplicates(nums):
    if not nums:
        return []
    left, right = 1, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        count = 0
        for i in nums:
            if i <= mid:
                count += 1
        if count <= mid:
            left = mid + 1
        else:
            right = mid
    return left

find_duplicates([1,1,2,3,1])