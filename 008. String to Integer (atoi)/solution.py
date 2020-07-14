import re


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        witht the use of the re package
        """
        min_limit = -(2 ** 31)
        max_limit = 2 ** 31 - 1
        p_num = re.findall(r"^[+-]?\d+", str.lstrip())
        ''''
        或者
        return max(min(int(p_num[0]), 2**31-1), -2**31) if p_num else 0
        '''
        if p_num:
            if int(p_num[0]) > max_limit:
                return max_limit
            elif int(p_num[0]) < min_limit:
                return min_limit
            else:
                return int(p_num[0])
        else:
            return 0


'''
Runtime: 32 ms, faster than 33.64% of Python online submissions for String to Integer (atoi).
Memory Usage: 12.9 MB, less than 15.79% of Python online submissions for String to Integer (atoi).
'''





if __name__ == '__main__':
    str = "   42"
    print(Solution().myAtoi(str))
