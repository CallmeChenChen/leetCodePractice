"""
in-place O(1) extra memory

nums = [3, 2, 2, 3] val = 3  output 2  length([2,2])

"""



class Solution(object):
    def removeElement(self, nums, val):
        """

        :param nums: list[int]
        :param val: int
        :return: int length
        """

        for idx in range(len(nums)):
            if nums[idx] == val:
                nums[idx] = 0
            else:
                nums[idx] = 1
        return sum(nums)

    def removeElement1(self, nums, val):
        # 双指针
        last = len(nums) - 1
        i = 0
        while i <= last:
            if val == nums[i]:
                nums[i], nums[last] = nums[last], nums[i]
                last -= 1
            else:
                i += 1
        return i

    def removeElement2(self, nums, val):
        i, last = 0, len(nums) - 1
        while i <= last:
            if val == nums[i]:
                nums[i], nums[last] = nums[last], nums[i]
                last -= 1
            else:
                i += 1
        return last + 1


if __name__ == '__main__':

    s = Solution()

    print(s.removeElement2([2,2,2,2], 2))
