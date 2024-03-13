class Solution(object):
    def containsDuplicate(self, nums):
        """
        Similar to 001
        1. traverse all the items of nums
            2. if it is already in set -> return True
            3. else -> store it into set
        4. return False

        Time: O(n) -- traverse once
        Space: O(n) -- for HashSet
        """
        checkSet = set()
        for element in nums:
            if element in checkSet:
                return True
            else:
                checkSet.add(element)
        return False
        