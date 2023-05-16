class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousMap = {}

        for i, num in enumerate(nums):
            # enumarate(array)
            difference = target - num
            if (difference in previousMap):
                # key in map
                return [previousMap[difference], i]
                # value in map
            else:
                previousMap[num] = i
                # insert into a map
        return