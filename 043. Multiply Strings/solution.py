class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        count1 = 0
        count2 = 0
        ans = 0
        for i in reversed(num2):
            for j in reversed(num1):
                ans += int(i) * int(j) * (10 ** count1) * (10 ** count2)
                if count1 < len(num1) - 1:
                    count1 += 1
                else:
                    count1 = 0
            count2 += 1
        return str(ans)


'''
Runtime: 444 ms, faster than 8.58% of Python online submissions for Multiply Strings.
Memory Usage: 12.8 MB, less than 35.06% of Python online submissions for Multiply Strings.
'''

if __name__ == '__main__':
    num1 = "123"
    num2 = "456"
    print(Solution().multiply(num1, num2))
