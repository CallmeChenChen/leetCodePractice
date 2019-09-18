"""
() {} []
判断括弧是不是一对[{()}]

栈
"""

class Solution(object):
    def isValid(self, s):
        stack = []
        # 这步很关键
        lookup = {"(": ")", "{": "}", "[": "]"}

        for parenthese in s:
            if parenthese in lookup.keys():
                stack.append(parenthese)
            else:
                # if len(stack) == 0:
                #     return False
                # elif lookup.get(stack[-1]) == parenthese:
                #     stack.pop()
                # else:
                #     return False

                if len(stack) == 0 or lookup.get(stack[-1]) != parenthese:
                    return False
                else:
                    stack.pop()

        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("]{"))
