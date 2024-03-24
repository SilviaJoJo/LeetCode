class Solution(object):
    def search(self, nums, target):
        """
        Similar to 153
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            # Base case
            if (left == right):
                if nums[left] == target:
                    return left
                return -1
            # Recursive case
            middle = (left + right) // 2
            if (nums[middle] >= nums[left]):
                if (target >= nums[left] and target <= nums[middle]):
                    right = middle
                else:
                    left = middle + 1
            else:
                if (target >= nums[middle] and target <= nums[right]):
                    left = middle
                else:
                    right = middle - 1
        