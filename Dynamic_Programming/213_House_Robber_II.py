class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        The key of this problem is how to utilize our previous code!
        Just consider several edge cases:
        1. the maximum result counts into both the end and the start
            1.1 quit the start
            1.2 quit the end
        2. the maximum result does not count into both the end and the start
            same as 1
        3. the input consists only one element

        Time: O(n)
        Space: O(1)
        """
        if len(nums) == 1:
            return nums[0]
        result1 = self.robHelper(nums[1:])
        result2 = self.robHelper(nums[:-1])
        return max(result1, result2)

        # the code from House Robber
    def robHelper(self, nums):
        rob1, rob2 = nums[-1], 0
        for i in range(len(nums) - 2, -1, -1):
            tmp = rob2
            rob2 = rob1
            rob1 = max(nums[i] + tmp, rob1)
        return rob1