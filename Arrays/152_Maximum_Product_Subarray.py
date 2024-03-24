class Solution(object):
    def maxProduct(self, nums):
        """
        Similar to 053
        1. traverse the input array once
        2. keep track of three variables: ans, currMax and currMin
            the trap here is that, currMax isn't necessarily the true maxVal
        3. handle the edge case (0) correctly

        Time: O(n)
        Space: O(1)
        """
        ans = max(nums)
        currMax = 1
        currMin = 1
        for num in nums:
            if (num == 0):
                currMax = 1
                currMin = 1
            else:
                possibleMax = num * currMax
                possibleMin = num * currMin
                currMax = max(possibleMax, possibleMin, num)
                currMin = min(possibleMax, possibleMin, num)
                ans = max(ans, currMax)
        return ans
