class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        1. do bottom-up, starting from the last index
        2. generalize the mechanism of comparison
        3. do double traversal

        Time: O(n^2)
        Space: O(n)
        """
        # initialize dp with minimum possible length
        dp = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        # after traversal, the 0th element isn't necessarily the greatest
        return max(dp)
        