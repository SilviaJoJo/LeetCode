class Solution(object):
    def threeSum(self, nums):
        """
        1. sort the original array
        2. traverse the sorted array, and for each element
            3. use double pointers to do another traversal: left and right
            4. adjust the position of left and right accordingly
            5. handle duplicates gracefully
        
        Time: O(n^2)
        Space: O(n) -- for sort (merge sort or timsort) and ansSet / ans
        """
        ansSet = set()
        nums.sort()
        for index, value in enumerate(nums):
            # this precheck was added to improve efficiency
            if (index > 0 and value == nums[index - 1]):
                continue
            left, right = index + 1, len(nums) - 1
            while left < right: # left and right cannot meet, because we want three lements
                currSum = value + nums[left] + nums[right]
                if not currSum:
                    ansSet.add((value, nums[left], nums[right]))
                    # continue to find other possible combinations
                    left += 1
                elif currSum < 0:
                    left += 1
                else:
                    right -= 1
        ans = [list(item) for item in ansSet]
        return ans
        