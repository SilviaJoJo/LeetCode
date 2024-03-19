class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        1. initialize a 2D matrix (M * N) with all 0s
        2. do bottom up, start from the lower right corner
        3. when we break the current problem into subproblems:
            4. if current is a match, go diagonal
            5. else -> go upper or left
        6. until we reach the upper left corner

        Time: O(mn)
        Space: O(mn)
        """
        # remember to leave space for "out-of-bound" grid!
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if (text1[i] == text2[j]):
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[0][0]