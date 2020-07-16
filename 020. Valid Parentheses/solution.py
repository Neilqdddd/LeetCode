class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []
        for i in s:
            if i in mapping:
                if stack:
                    last_element = stack.pop()
                else:
                    last_element = '@'
                if mapping[i] != last_element:
                    return False
            else:
                stack.append(i)
        return not stack


if __name__ == '__main__':
    s = "([)]"
    print(Solution().isValid(s))
