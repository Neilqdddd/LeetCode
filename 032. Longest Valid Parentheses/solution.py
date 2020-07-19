class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max = 0
        stack = []
        cur_len = 0
        for p in s:
            if p == '(':
                stack.append(cur_len)
                cur_len = 0
            elif p == ')':
                if stack:
                    cur_len += stack.pop() + 2
                    max = max(max, cur_len)
                else:
                    cur_len = 0
        return max


if __name__ == '__main__':
    s = "(()"
    print(Solution().longestValidParentheses(s))
