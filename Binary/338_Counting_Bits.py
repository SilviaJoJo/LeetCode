class Solution(object):
    def countBits(self, n):
        """
        1. use dynamic programming with an array
            dp[1] = 1 + dp[0] = 1 + dp[1 - 1]
            dp[2] = 1 + dp[0] = 1 + dp[2 - 2]
            dp[3] = 1 + dp[1] = 1 + dp[3 - 2]
            dp[4] = 1 + dp[0] = 1 + dp[4 - 4]
        2. use iteration
        3. use a variable to keep track of the largest 2^n

        Time: O(n)
        Space: O(n)
        """
        dp = [0] * (n + 1)
        largest2N = 1

        for i in range(1, n + 1):
            # double largest2N when applicable
            if (largest2N * 2 == i):
                largest2N *= 2
            dp[i] = 1 + dp[i - largest2N]
        return dp
        