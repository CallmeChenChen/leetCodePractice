"""
longest common prefix
最长单词的相同长度
input 'flower' 'flow' 'flight' output:'fl'
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """

        :param strs: list[str]
        :return: str
        """
        if not strs:
            return ""

        for i in range(len(strs[0])):
            for s in strs[1:]:
                if i >= len(s) or s[i] != strs[0][i]:
                    return strs[0][:i]
        return ""

    def longestCommonPrefix1(self, strs):
        i = 0
        while True:
            try:
                tmp_sets = set(string[i] for string in strs)
                if len(tmp_sets) == 1:
                    i += 1
                else:
                    break
            except Exception as e:
                print(e)
                break
        return strs[0][:i]

if __name__ == '__main__':
    
    s = Solution()
    print(s.longestCommonPrefix(['abdcdd', 'abd', 'abdbbb']))
