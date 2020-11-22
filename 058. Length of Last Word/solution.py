class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split()
        if not len(s):
            return 0
        return len(s[-1])


if __name__ == '__main__':
    s = "Hello World"
    print(Solution().lengthOfLastWord(s))
