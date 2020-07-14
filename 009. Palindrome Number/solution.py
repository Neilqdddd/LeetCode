class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        x = str(x)
        i = 0
        j = len(x) - 1
        while i < j:
            if x[i] != x[j]:
                return False
            i += 1
            j -= 1
        return True


'''
Runtime: 64 ms, faster than 47.10% of Python online submissions for Palindrome Number.
Memory Usage: 12.7 MB, less than 49.65% of Python online submissions for Palindrome Number.
'''

'''
或者
'''


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        strg = str(x)
        if x >= 0:
            rev = strg[::-1]
        else:
            return False
        if rev == strg:
            return True
        else:
            return False


'''
Runtime: 44 ms, faster than 91.75% of Python online submissions for Palindrome Number.
Memory Usage: 12.9 MB, less than 5.15% of Python online submissions for Palindrome Number.
'''

if __name__ == '__main__':
    x = 121
    print(Solution().isPalindrome(x))
