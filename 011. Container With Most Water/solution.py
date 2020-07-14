class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p = 0
        q = len(height) - 1
        ans = []
        while p < q:
            # 左边界大于右边界，移动右边界
            if height[p] >= height[q]:
                ans.append(height[q] * (q - p))
                q -= 1
            # 反之右边界大于左边界，移动左边界
            else:
                ans.append(height[p] * (q - p))
                p += 1
        return max(ans)


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution().maxArea(height))
