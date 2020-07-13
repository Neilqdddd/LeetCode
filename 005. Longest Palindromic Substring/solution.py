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
Manacher's Algorithm
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        思想为找到中心点，然后确定中心点的对称半径。
        如果新的潜在对称点超过以知的点，比较超过已知半径点。
        重新分配中心点，循环
        reference：https://www.youtube.com/watch?v=nbTSfrEfo6M
        """

        t = '#'.join('${}@'.format(s))
        print(t)
        l = len(t)
        # 储存对称半径的list
        p = [0 for i in range(l)]

        # c 为回文字符的中心点
        # r 为右边界
        c = r = 0

        for i in range(1, l - 1):
            '''
            i 在对称的右边界中的话，已经判定为对称
            直接赋值对左对称点的对称半径
            $#a#b#c#b#a#@
            右边的b即可赋值左边b的对称半径3
            '''

            if r >= i:
                p[i] = min(r - i, p[2 * c - i])
            '''
            扩张，假设这个点为一个新的中心点，
            镜像的对称半径为, p[i] = p[2*c - i]
            下一个扩张的点为 i + 已知的对称半径 + 1， T [i+p[i]+1]
            潜在对称点为 i - 已知对称半径 -1 
            潜在对称点为 T[i - p[i] -1] 
            '''
            while t[i + p[i] + 1] == t[i - p[i] - 1]:
                p[i] += 1

            '''
            判断更新 中心点c 与 右边界r
            如果 i + p[i] > r i+新对称半径超过原来的r
            i 为新的中心点c ， i+p[i]为新的对称半径r
            '''
            if i + p[i] > r:
                c, r = i, i + p[i]
        '''
        例如 p 得出[0, 0, 1, 0, 3, 0, 3, 0, 1, 0, 1, 0, 0]
        找到最大值的点为中心， 与最大值点的位置的点为有效半径
        （中心点-有效半径）//2 得出在原来s中的位置
        '''
        center, center_r = max(enumerate(p), key=lambda x: x[1])
        return s[(center - center_r) // 2:(center + center_r) // 2]

'''
Runtime: 96 ms, faster than 96.70% of Python online submissions for Longest Palindromic Substring.
Memory Usage: 12.9 MB, less than 33.94% of Python online submissions for Longest Palindromic Substring.
'''


if __name__ == '__main__':
    s = 'babad'
    print(Solution().longestPalindrome(s))
