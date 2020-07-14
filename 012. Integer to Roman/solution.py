class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        buret force
        """
        ans = ''
        a1 = num // 1000
        ans += a1 * 'M'
        num = num % 1000

        a2 = num // 100
        if a2 >= 5:
            if a2 == 9:
                ans += 'CM'
            else:
                ans += 'D' + (a2 - 5) * 'C'
        else:
            if a2 == 4:
                ans += 'CD'
            else:
                ans += a2 * 'C'
        num = num % 100

        a3 = num // 10
        if a3 >= 5:
            if a3 == 9:
                ans += 'XC'
            else:
                ans += 'L' + (a3 - 5) * 'X'
        else:
            if a3 == 4:
                ans += 'XL'
            else:
                ans += a3 * 'X'
        num = num % 10

        if num >= 5:
            if num == 9:
                ans += 'IX'
            else:
                ans += 'V' + (num - 5) * 'I'
        else:
            if num == 4:
                ans += 'IV'
            else:
                ans += num * 'I'
        return ans


'''
Runtime: 48 ms, faster than 44.90% of Python online submissions for Integer to Roman.
Memory Usage: 12.9 MB, less than 8.75% of Python online submissions for Integer to Roman.
'''


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        more simple buret force
        """
        ans = ''
        romandict = {1000: 'M',
                     900: 'CM',
                     500: 'D',
                     400: 'CD',
                     100: 'C',
                     90: 'XC',
                     50: 'L',
                     40: 'XL',
                     10: 'X',
                     9: 'IX',
                     5: 'V',
                     4: 'IV',
                     1: 'I'
                     }
        for key, value in romandict.items():
            ans += value * (num // key)
            num %= key
        return ans


'''
Runtime: 88 ms, faster than 11.38% of Python3 online submissions for Integer to Roman.
Memory Usage: 14.1 MB, less than 5.27% of Python3 online submissions for Integer to Roman.
'''

'''
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
'''

if __name__ == '__main__':
    num = 4
    print(Solution().intToRoman(num))
