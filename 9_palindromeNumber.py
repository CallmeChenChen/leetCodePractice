"""
palindrome number(easy)
回文
121 True
-121 False
"""


class Solution:
    def isPalindrome(self, x):
        """

        :param x: int
        :return:
        """
        num = 0
        x_ = x
        if x < 0:
            return False
        else:
            while x_ != 0:
                tmp = x_ % 10
                num = num * 10 + tmp
                x_ = x_ // 10

            return True if num == x else False


if __name__ == '__main__':

    s = Solution()
    print(s.isPalindrome(1211))
