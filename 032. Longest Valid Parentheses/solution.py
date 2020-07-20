class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        stack = []
        cur_len = 0
        for p in s:
            if p == '(':
                stack.append(cur_len)
                cur_len = 0
            elif p == ')':
                if stack:
                    cur_len += stack.pop() + 2
                    max_len = max(max_len, cur_len)
                else:
                    cur_len = 0
        return max_len


'''
Runtime: 52 ms, faster than 37.43% of Python online submissions for Longest Valid Parentheses.
Memory Usage: 13.1 MB, less than 76.92% of Python online submissions for Longest Valid Parentheses.
'''

if __name__ == '__main__':
    s = "(()"
    print(Solution().longestValidParentheses(s))
