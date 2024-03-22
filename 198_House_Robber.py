class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        1. my initial thought was to initialize a dp array
        2. after examing the comparison process (which only involves two items)
            -> change the whole list into only two variables
            -> improved performance
        
        Time: O(n)
        Space: O(1)
        """
        rob1, rob2 = nums[-1], 0
        for i in range(len(nums) - 2, -1, -1):
            tmp = rob2
            rob2 = rob1
            rob1 = max(nums[i] + tmp, rob1)
        return rob1
        