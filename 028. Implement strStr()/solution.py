'''
slice
'''


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l, n = len(needle), len(haystack)

        for start in range(n - l + 1):
            if haystack[start:start + l] == needle:
                return start
        return -1


'''
two points
'''


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l, n = len(needle), len(haystack)
        if l == 0:
            return 0
        i = 0
        while i < n - l + 1:
            # find the first match char
            while i < n - l + 1 and haystack[i] != needle[0]:
                i += 1

            # find the max string
            curr = p = 0
            while p < l and i < n and haystack[i] == needle[p]:
                i += 1
                p += 1
                curr += 1
            if curr == l:
                return i - l
            i = i - curr + 1
        return -1


'''
Runtime: 24 ms, faster than 52.25% of Python online submissions for Implement strStr().
Memory Usage: 13.1 MB, less than 51.13% of Python online submissions for Implement strStr().
'''

if __name__ == '__main__':
    nums = "hello"
    val = "ll"
    print(Solution().strStr(nums, val))
