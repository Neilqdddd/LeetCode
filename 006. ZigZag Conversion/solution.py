class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        思想每行建立一个list内含numRows的小list，然后依次把内容填入相对应的小list中
        a1          g
        b2      f6
        c3  e5
        d4

        每个cycle为 2 * numRows -2
        a余数1                g
        b余数2        f余数0
        c余数3  e余数5
        d余数4

        当余数小于numRows 时为 list[numRows].append(str)
        当余数大于numRows 时为 比如 e 余数为 5 是倒数第二行， list[-(i - numRows) - 1].append(str)

        然后导出list中的所有字符为答案
        """
        if numRows == 1: return s
        ans = ''
        cycle = 2 * numRows - 2
        lst = [[] for i in range(0, numRows)]
        for index, l in enumerate(s):
            i = (index + 1) % (cycle)
            if i > 0 and i <= numRows:
                lst[i - 1].append(l)
            elif i > numRows:
                lst[-(i - numRows) - 1].append(l)
            elif i == 0:
                lst[1].append(l)

        for a in lst:
            for str in a:
                ans+=str
        return ans

'''
Not perfect not easy to understand
Runtime: 72 ms, faster than 48.60% of Python3 online submissions for ZigZag Conversion.
Memory Usage: 13.9 MB, less than 42.67% of Python3 online submissions for ZigZag Conversion.
'''


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 4
    print(Solution().convert(s, numRows))
