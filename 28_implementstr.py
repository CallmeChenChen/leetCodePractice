"""
implement Str

haystack hello  needle ll 2
haystack aaaa  needle bba -1

"""


class Solution(object):

    def implementStr(self, haystack, needle):

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i+len(needle)] == needle:
                return i

        return -1



if __name__ == '__main__':

    s = Solution()
    print(s.implementStr('hello', 'aa'))