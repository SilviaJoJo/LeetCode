class Solution(object):
    def missingNumber(self, nums):
        """
        My own solution: naive, without binary -- simplified according to NeetCode
        
        Time: O(1)
        Space: O(1)
        """
        ans = len(nums)
        for i in range(len(nums)):
            ans += (i - nums[i])
        return ans