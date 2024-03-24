class Solution(object):
    def maxProfit(self, prices):
        """
        1. use double pointers to traverse the array: left and right
        2. use another variable to keep track of the maximum profit

        Time: O(n) -- traverse once
        Space: O(1) -- no extra data structures
        """
        left = 0
        right = 1
        maxProfit = 0
        while (right < len(prices)):
            if (prices[left] > prices[right]):
                left = right # start over from a new low price
            else:
                maxProfit = max(maxProfit, prices[right] - prices[left])
            right = right + 1
        return maxProfit
        