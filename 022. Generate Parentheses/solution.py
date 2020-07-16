class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * n:
                ans.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)

        backtrack()
        return ans


'''
Runtime: 28 ms, faster than 40.21% of Python online submissions for Generate Parentheses.
Memory Usage: 12.9 MB, less than 40.13% of Python online submissions for Generate Parentheses.
'''

if __name__ == '__main__':
    n = 3
    print(Solution().generateParenthesis(n))
