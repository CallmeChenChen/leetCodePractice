# -*- coding: utf-8 -*-
# @Author : zhaochen
# @Date   : 2019/10/4
# @File   : 04_01_Search.py.py


# 二分查找
#Binary Search (recursive)
def binary_search_rec(nums, val):
    # if len(nums) == 0:
    #     return -1
    def helper(left, right):
        if left > right:
            return -1
        mid = left + (right - left) // 2
        if nums[mid] == val:
            return mid
        elif nums[mid] > val:
            return helper(left, mid - 1)
        else:
            return helper(mid + 1, right)

    return helper(0, len(nums)-1)
# O(logN)
def binary_search_iter(nums, val):
    left, right = 0 , len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == val:
            return mid
        elif nums[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    return -1



import unittest

class TestBinarySearch1(unittest.TestCase):
    def setUp(self):
        self._f = binary_search_rec

    def test_empty(self):
        alist = []
        r = self._f(alist, 5)
        self.assertEqual(-1, r)

    def test_one(self):
        alist = [1]
        r = self._f(alist, 0)
        self.assertEqual(-1, r)
        r = self._f(alist, 1)
        self.assertEqual(0, r)

    def test_two(self):
        alist = [1, 10]
        r = self._f(alist, 0)
        self.assertEqual(-1, r)
        r = self._f(alist, 1)
        self.assertEqual(0, r)
        r = self._f(alist, 2)
        self.assertEqual(-1, r)
        r = self._f(alist, 10)
        self.assertEqual(1, r)
        r = self._f(alist, 11)
        self.assertEqual(-1, r)

    def test_multiple(self):
        alist = [1, 2, 3, 4, 5]
        r = self._f(alist, 5)
        self.assertEqual(4, r)
        r = self._f(alist, 4)
        self.assertEqual(3, r)
        r = self._f(alist, 2)
        self.assertEqual(1, r)
        r = self._f(alist, 1)
        self.assertEqual(0, r)
        r = self._f(alist, 6)
        self.assertEqual(-1, r)
        r = self._f(alist, 0)
        self.assertEqual(-1, r)

    def test_duplicate(self):
        alist = [1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 4, 5, 5, 5]
        r = self._f(alist, 5)
        self.assertEqual(5, alist[r])
        r = self._f(alist, 4)
        self.assertEqual(4, alist[r])
        r = self._f(alist, 2)
        self.assertEqual(2, alist[r])
        r = self._f(alist, 3)
        self.assertEqual(3, alist[r])
        r = self._f(alist, 1)
        self.assertEqual(1, alist[r])
        r = self._f(alist, 6)
        self.assertEqual(-1, r)
        r = self._f(alist, 0)
        self.assertEqual(-1, r)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
