class Solution(object):
    def hammingWeight(self, n):
        """
        Time: O(1) -- the while loop gets executed for precisely 32 times
        Space: O(1)
        """
        totalOnes = 0
        while n:
            totalOnes += n % 2
            n = n >> 1
        return totalOnes
        