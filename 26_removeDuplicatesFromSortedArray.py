"""
in-place with O(1) extra memory

nums = [1,1,2]  1,2 return 2

nums = [0,0,1,1,2,2,3,3,4]  0,1,2,3,4 return 5

:return length

"""

class Solution:

    def removeDuplicates(self, nums):
        """

        :param nums: list[int]
        :return: int length
        """
        if not nums:
            return 0
        count = 0
        for i in range(len(nums)):
            if nums[i] != nums[count]:
                count += 1
                nums[count] = nums[i]

        return count + 1


if __name__ == '__main__':

    s = Solution()

    print(s.removeDuplicates())