class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = []
        letterdict = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
                      '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                      '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                      '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        def combine(combination, next_digit):
            if len(next_digit) == 0:
                ans.append(combination)
            else:
                for letter in letterdict[next_digit[0]]:
                    combine(combination + letter, next_digit[1:])

        if digits:
            combine("", digits)
        return ans


'''
Runtime: 16 ms, faster than 86.40% of Python online submissions for Letter Combinations of a Phone Number.
Memory Usage: 12.9 MB, less than 6.91% of Python online submissions for Letter Combinations of a Phone Number.
'''

if __name__ == '__main__':
    digits = "23"
    print(Solution().letterCombinations(digits))
