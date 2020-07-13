'''
Dynamic programming
Time Complexity: O(n2)
Space Complexity: O(n2)
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return s
        ans = ""
        matrix = [[None for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            for j in range(i + 1):
                if i == j:
                    matrix[i][j] = True
                elif i == j + 1:
                    matrix[i][j] = (s[i] == s[j])
                else:
                    matrix[i][j] = (matrix[i - 1][j + 1] and s[i] == s[j])
                if matrix[i][j] and i - j + 1 > len(ans):
                    ans = s[j:i + 1]
        return ans


'''
Runtime: 5988 ms, faster than 11.53% of Python online submissions for Longest Palindromic Substring.
Memory Usage: 21.5 MB, less than 6.74% of Python online submissions for Longest Palindromic Substring.
'''

'''
Dynamic programming improve space
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return s
        ans = ""
        matrix = [None for i in range(len(s))]
        for i in range(len(s)):
            for j in range(i + 1):
                if i == j:
                    matrix[j] = True
                elif i == j + 1:
                    matrix[j] = (s[i] == s[j])
                else:
                    matrix[j] = (matrix[j + 1] and s[i] == s[j])
                if matrix[j] and i - j + 1 > len(ans):
                    ans = s[j:i + 1]
        return ans


'''
Runtime: 3336 ms, faster than 31.99% of Python online submissions for Longest Palindromic Substring.
Memory Usage: 12.8 MB, less than 59.68% of Python online submissions for Longest Palindromic Substring.
'''

'''
Around the center
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return s
        ans = ''
        for i in range(len(s)):
            res1 = self.Expand(s, i, i)  # if odd
            res2 = self.Expand(s, i, i + 1)  # if even
            temp = res1 if (len(res1) > len(res2)) else res2
            ans = temp if (len(temp) > len(ans)) else ans
        return ans

    def Expand(self, s, p, q):
        '''
        s中p，g为起点，比较是否相同
        '''
        while (p >= 0 and q < len(s)):
            if s[p] == s[q]:
                p -= 1
                q += 1
            else:
                break
        return s[p + 1: q]


'''
Runtime: 940 ms, faster than 59.74% of Python online submissions for Longest Palindromic Substring.
Memory Usage: 12.7 MB, less than 75.65% of Python online submissions for Longest Palindromic Substring.
'''

'''
Manacher's Algorithm still working on that
'''

if __name__ == '__main__':
    s = 'babad'
    print(Solution().longestPalindrome(s))
