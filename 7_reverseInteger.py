'''
reverse integer (easy)
 123 321
 -123 -321
 120 21

[-2**31, 2**31-1]
'''



class Solution(object):
    def reverse(self, x):
        """

        :param x:int
        :return:
        """
        num = 0

        a = abs(x)

        while(a != 0):

            tmp = a % 10 # 取模
            # print('tmp', tmp)
            num = num * 10 + tmp
            # print('num', num)
            a = a // 10 # 取整
            # print('a', a)
            # print('-'*10)

        if x > 0 and num < 2**31 - 1:
            return num
        elif x < 0 and num >= -2**31:
            return -num
        else:
            return 0

if __name__ == '__main__':

    s = Solution()
    print(s.reverse(123))