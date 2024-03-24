class Solution(object):
    def missingNumber(self, nums):
        """
        Use the binary property:
        1. n xor n = 0
        2. n xor n xor m = m (the order doesn't matter)

        Time: O(1)
        Space: O(1)
        """
        missing = 0
        for i, num in enumerate(nums):
            missing = missing ^ i ^ num
        return missing ^ len(nums)