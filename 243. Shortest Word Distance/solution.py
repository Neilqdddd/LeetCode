class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        lt_1 = []
        lt_2 = []
        ans = len(words)

        for index, value in enumerate(words):
            if value == word1:
                lt_1.append(index)
            elif value == word2:
                lt_2.append(index)
            if lt_1 and lt_2:
                ans = min(ans, abs(lt_1[-1] - lt_2[-1]))
        return ans


if __name__ == '__main__':
    words = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "coding"
    word2 = "practice"
    print(Solution().shortestDistance(words, word1, word2))
