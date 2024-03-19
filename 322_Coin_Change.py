class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        1. this time in arriving each value, we need to do many comparisons
            -> use a dp array instead of a few variables
        2. bottom up, from 0 to amount

        Time: O(amount * len(coins))
        Space: O(amount)
        """
        # initialize dp with each value to be the impossible max
        # must be impossible, otherwise messed up with -1 case
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        if dp[amount] < amount + 1: # we find a solution
            return dp[amount]
        return -1