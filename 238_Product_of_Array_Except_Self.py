class Solution(object):
    def productExceptSelf(self, nums):
        """
        1. use an array to store prefix multiplication -> [1, 2, 6, 12]
        2. use an array to store postfix multiplication -> [24, 24, 12, 4]
        3. combine two arrays together to produce result -> [24, 12, 8, 6]
        4. improve the original algorithm to in-place modification -> [1, 1, 2, 6] * [24, 12, 4, 1]

        Time: O(n)
        Space: O(n)
        """
        prefix = 1
        postfix = 1
        ans = [1] * len(nums)
        for i in range(len(nums)):
            ans[i] = prefix
            prefix = prefix * nums[i]
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]
        return ans
        