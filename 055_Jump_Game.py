class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        given the current index and the current step, we have a range of places
        that we can reach within one jump, and there is thus an upper bound
        if goal is beyond this target, we need to do further jumps
        so our purpose of dynamic programming is to gradually shifting our goal leftwards
        until it enter our range within the first jump (from 0th index)

        Time: O(n)
        Space: O(1)
        """
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return not goal