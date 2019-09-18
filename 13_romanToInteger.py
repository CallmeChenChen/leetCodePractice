"""

I:1
V:5  IV:4
X:10 IX:9
L:50
C:100
D:500
M:1000

'III' 3

'MCMXCIV':1000+900+90+4

当前字母的前后一位数字的大小关系
"""

class Solution(object):

    def romanToInt(self, s):
        """

        :param s: str
        :return: int
        """
        numeral_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0

        for i in range(len(s)):
            # 注意数组越界问题
            if (i < len(s)-1) and numeral_map[s[i]] < numeral_map[s[i+1]]:
                result += (numeral_map[s[i+1]] - numeral_map[s[i]]) - numeral_map[s[i+1]]
            else:
                result += numeral_map[s[i]]

        return result


if __name__ == '__main__':

    s = Solution()
    print(s.romanToInt('MCMXCIV'))
    print(s.romanToInt('III'))