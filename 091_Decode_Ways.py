class Solution:
    def numDecodings(self, s: str) -> int:
        """
        I really love this problem because it's quite classic!
        we use the dynamic programming method as a combination of recursion + caching
        which utilizes the data structure of map instead of list

        Time: O(n)
        Space: O(n)
        """
        # we insert a default value for the base case/ end of recursion
        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue
            # check 1-digit case
            result = dp[i + 1]
            # check 2-digit case
            if i + 2 in dp and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                result += dp[i + 2]
            dp[i] = result
        return dp[0]
