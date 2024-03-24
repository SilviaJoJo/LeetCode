class Solution(object):
    def findMin(self, nums):
        """
        1. Binary search algorithm -> O(log n) time
        2. uses double pointers to traverse the array: left and right

        Time: O(log n)
        Space: O(1)
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            # Base case: already sorted subarray
            if (nums[left] <= nums[right]):
                return nums[left]
            # Recursive case
            middle = (left + right) // 2
            if (nums[middle] >= nums[left]):
                left = middle + 1
            else:
                right = middle
        