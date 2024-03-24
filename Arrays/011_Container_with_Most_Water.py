class Solution(object):
    def maxArea(self, height):
        """
        1. use double pointers: right and left to traverse the input array only once
            2. adjust them based on height
        3. keep track of an additional variable: currMax

        Time: O(n)
        Space: O(1)
        """
        currMax = 0
        left, right = 0, len(height) - 1
        while left < right: # left and right cannot meet, otherwise the area will be 0
            area = (right - left) * min(height[left], height[right])
            currMax = max(currMax, area)
            # find a left that is not too bad -> loose constraint
            if height[left] < height[right]:
                left += 1
            # find an optimal right for the given left -> strict constraint
            else:
                right -= 1
        return currMax
        