class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        romandict = {'M': 1000,
                     'CM': 900,
                     'D': 500,
                     'CD': 400,
                     'C': 100,
                     'XC': 90,
                     'L': 50,
                     'XL': 40,
                     'X': 10,
                     'IX': 9,
                     'V': 5,
                     'IV': 4,
                     'I': 1}
        i = 0
        while i < len(s):
            try:
                a = romandict[s[i] + s[i + 1]]
                ans += a
                i += 2
            except:
                b = romandict[s[i]]
                ans += b
                i += 1
        return ans


'''
Runtime: 48 ms, faster than 49.52% of Python online submissions for Roman to Integer.
Memory Usage: 12.9 MB, less than 7.73% of Python online submissions for Roman to Integer.
'''


# or
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        romandict = {'M': 1000,
                     'CM': 900,
                     'D': 500,
                     'CD': 400,
                     'C': 100,
                     'XC': 90,
                     'L': 50,
                     'XL': 40,
                     'X': 10,
                     'IX': 9,
                     'V': 5,
                     'IV': 4,
                     'I': 1}

        i = 0
        while i < len(s):
            try:
                a = romandict[s[i] + s[i + 1]]
            except:
                a = 0
            b = romandict[s[i]]
            if a > b:
                ans += a
                i += 2
            else:
                ans += b
                i += 1
        return ans


'''
Runtime: 60 ms, faster than 25.74% of Python online submissions for Roman to Integer.
Memory Usage: 12.7 MB, less than 61.09% of Python online submissions for Roman to Integer.
'''

if __name__ == '__main__':
    s = "LVIII"
    print(Solution().romanToInt(s))
