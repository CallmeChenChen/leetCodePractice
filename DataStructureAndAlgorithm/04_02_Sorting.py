# -*- coding: utf-8 -*-
# @Author : zhaochen
# @Date   : 2019/10/4
# @File   : 04_02_Sorting.py

# 对数组进行排序

# bubble sort 冒泡
def bubble_sort(nums, is_reverse=False):
    if not nums:
        return []
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    if is_reverse:
        return nums[::-1]
    else:
        return nums

bubble_sort([3,2,4,1,0,1], True)
bubble_sort([0,0,0], True)


# selection sort 选择

def selection_sort_min(nums):
    if not nums:
        return []
    for i in range(len(nums)):
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[min_idx], nums[i] = nums[i], nums[min_idx]
    return nums
selection_sort_min([1,2,3,2,1,7,2])

def selection_sort_max(nums):
    if not nums:
        return []
    for i in range(len(nums)-1, -1, -1):
        max_idx = i
        for j in range(i):
            if nums[j] > nums[max_idx]:
                max_idx = j
        nums[max_idx], nums[i] = nums[i], nums[max_idx]
    return nums
selection_sort_max([8,1,2,3,2,1,7,2])

# insert sort 插入
def insert_sort(nums):
    if not nums:
        return []
    for i in range(1, len(nums)):
        unsort_idx = i
        # 对之前的重新排序
        while unsort_idx > 0 and nums[unsort_idx - 1] > nums[unsort_idx]:
            nums[unsort_idx - 1], nums[unsort_idx] = nums[unsort_idx], nums[unsort_idx - 1]
            unsort_idx = unsort_idx - 1
    return nums

insert_sort([8,1,2,3,2,1,7,2])

# shell sort

# count sort 计数排序(桶排序)

def count_sort(nums):
    if not nums:
        return []
    # minimum, maximum = min(nums), max(nums)
    _min, _max = nums[0], nums[0]
    for i in nums:
        if _min > i:
            _min = i
        if _max < i:
            _max = i
    k = _max - _min + 1
    counts = [0] * k
    for i in range(len(nums)):
        counts[nums[i] - _min] = counts[nums[i] - _min] + 1
    # tmp = []
    # for i in range(len(counts)):
    #     tmp.extend([_min + i] * counts[i])
    # return tmp
    pos = 0
    for i in range(k):
        for j in range(counts[i]):
            nums[pos] = _min + i
            pos += 1
    return nums

count_sort([8,1,2,3,2,1,7,2,1,1,12,2,3,4,4,4])
count_sort([1,2,3,4])
count_sort([1])
# radix sort

# merge sort 归并排序

def merge_sort(nums):
    if not nums:
        return []
    # 对每2个子集排序合并
    def _merge_sorted(nums1, nums2):
        if nums1[0] > nums2[-1]:
            return nums2 + nums1
        if nums1[-1] < nums2[0]:
            return nums1 + nums2
        result = []
        while len(nums1) > 0 and len(nums2) > 0:
            if nums1[0] < nums2[0]:
                result.append(nums1[0])
                nums1.remove(nums1[0])
            else:
                result.append(nums2[0])
                nums2.remove(nums2[0])
        if len(nums1) != 0:
            # result += nums1
            result.extend(nums1)
        if len(nums2) != 0:
            # result += nums2
            result.extend(nums2)
        return result

    def _merge(nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        a = _merge(nums[:mid])
        b = _merge(nums[mid:])
        return _merge_sorted(a, b)

    nums = _merge(nums)

    return nums

merge_sort([1,2,3,2,1,7,2,1,1,12,2,3,4,4,4])

# quick sort

def quick_sort(nums):
    if not nums:
        return []
    def _partition(nums):
        if len(nums) <= 1:
            return nums
        pivot = nums[0]
        left = _partition([i for i in nums[1:] if i < pivot])
        right = _partition([i for i in nums[1:] if i >= pivot])
        return left + [pivot] + right

    nums = _partition(nums)

    return nums

quick_sort([1,6,3,5,1,7,2,10,12,2,3,4])