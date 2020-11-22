class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        ans = []
        '''
        一共三种情况
        1. [1,3],[2,4] 合并后为[1,4]
        2. [1,5],[2,3] 合并后[1,5]
        3. [1,2],[3,4] 合并后不变
        1,2 可以简单的把区间的后一位，使用max(ans[-1][1], interval[-1])
        '''
        for interval in intervals:
            if not ans or ans[-1][-1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][-1] = max(ans[-1][1], interval[-1])
        return ans


if __name__ == '__main__':
    intervals = [[1, 3], [8, 10], [15, 18], [2, 6]]
    print(Solution().merge(intervals))
