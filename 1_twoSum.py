'''

1. two sum
'''



class Solution(object):
    def twoSum(self, nums, target):
        tmp = {}
        for i in nums:
            if target - i in tmp:
                first_index = tmp.get(target - i)
                second_index = len(tmp)
                return first_index, second_index
            tmp[i] = len(tmp)


if __name__ == '__main__':

    nums = [2, 7, 11, 15]
    target = 18

    s = Solution()
    r = s.twoSum(nums=nums, target=target)

    print(r)