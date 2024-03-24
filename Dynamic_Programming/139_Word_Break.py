class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        1. do bottom up: starting from the last index (one extra element)
        2. only mark several elements as True
        3. return the 0th element

        Time: O(mn)
        Space: O(m)
        """
        length = len(s)
        dp = [False] * (length + 1)
        dp[-1] = True
        for i in range(length, -1, -1):
            for word in wordDict:
                if i + len(word) <= length and s[i : i+len(word)] == word:
                    dp[i] = dp[i + len(word)]
                    if dp[i]:
                        break
        return dp[0]
        