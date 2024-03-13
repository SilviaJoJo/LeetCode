class Solution(object):
    def maxSubArray(self, nums):
        """
        1. traverse the input array only once
        2. keep track of two additional variables: currSum and maxSum
        3. when currSum becomes negative, reset it to be 0
        4. everytime we update currSum (except reset), compare it with maxSum

        Time: O(n)
        Space: O(1)
        """
        currSum = 0
        maxSum = nums[0]
        for element in nums:
            if (currSum < 0):
                currSum = 0
            currSum += element
            maxSum = max(currSum, maxSum)
        return maxSum
        