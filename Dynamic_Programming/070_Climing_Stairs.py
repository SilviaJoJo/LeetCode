class Solution:
    def climbStairs(self, n: int) -> int:
        """
        1. the intuitive solution is to use recursion
        2. to improve performance, we do caching/ memoization
        3. use an array: dp to store answers for sub-problems
        4. further improving: keep track of two variables, instead of a whole array

        Time: O(n)
        Space: O(1)
        """
        # start from bottom to top
        # dp[-2] = 1 (called one), dp[-1] = 1 (called two)
        one, two = 1, 1
        for _ in range(n - 1):
            tmp = two
            two = one
            one = tmp + two
        return one