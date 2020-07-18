class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        index = []
        divisor_lst = []

        d = 2
        i = 1
        ans = 0
        if dividend > 0:
            d -= 1
            dividend = -dividend
        if divisor > 0:
            d -= 1
            divisor = -divisor

        '''
        思路生成一个divisor 2的倍数的list
        假如 dividend 为 10
        加入 divisor 为 3
        生成一个lis1t[3, 6, 12, 24, 48]
        另一个list2储存2的倍数[1, 2, 4, 8， 16]
        '''
        while divisor >= dividend:
            divisor_lst.append(divisor)
            index.append(i)
            i *= 2
            divisor *= 2
        '''
        假如 dividend 为 10
        加入 divisor 为 3
        生成一个list[3, 6]
        另一个list储存2的倍数[1, 2]
        从6开始向前
        然后 + list2中的数字
        '''
        for n in reversed(range(len(divisor_lst))):
            if divisor_lst[n] >= dividend:
                dividend -= divisor_lst[n]
                ans += index[n]
        if d == 1:
            return max(ans * -1, -2 ** 31)
        else:
            return min(ans, 2 ** 31 - 1)


'''
Runtime: 20 ms, faster than 80.69% of Python online submissions for Divide Two Integers.
Memory Usage: 12.7 MB, less than 55.36% of Python online submissions for Divide Two Integers.
'''

if __name__ == '__main__':
    dividend = -2147483648
    divisor = -1
    print(Solution().divide(dividend, divisor))
