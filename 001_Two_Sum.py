class Solution(object):
    def twoSum(self, nums, target):
        """
        1. traverse the input array for once, retrieve value and index
            2. if target - value in map -> return
            3. else -> store the current pair into map

        Time: O(n) -- traverse once
        Space: O(n) -- for HashMap
        """
        checkMap = {} # initialized a map, whose items are value : index
        for index, value in enumerate(nums):
            match = target - value
            if match in checkMap:
                return [checkMap[match], index]
            else:
                checkMap[value] = index
        