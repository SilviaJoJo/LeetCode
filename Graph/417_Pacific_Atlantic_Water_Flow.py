class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        1. have two sets, one for Pacific, one for Atlantic
        2. add items to those two sets that are at the boundry
        3. add inner items
            2 & 3 should be implemented in combination of recursion and iteration
        4. return with iteration

        Time: O(mn)
        Space: O(mn)
        """
        m = len(heights)
        n = len(heights[0])
        pacific, atlantic = set(), set() # stores tuples which are immutable

        def paHelper(r, c, visited, h):
            # Base case: invalid
            if (r, c) in visited or r < 0 or c < 0 or r >= m or c >= n or heights[r][c] < h:
                return
            # Recursive case
            visited.add((r, c))
            # all higher neighbors are also valid
            paHelper(r - 1, c, visited, heights[r][c])
            paHelper(r + 1, c, visited, heights[r][c])
            paHelper(r, c - 1, visited, heights[r][c])
            paHelper(r, c + 1, visited, heights[r][c])
    
        for i in range(m):
            paHelper(i, 0, pacific, 0)
            paHelper(i, n - 1, atlantic, 0)
        for i in range(n):
            paHelper(0, i, pacific, 0)
            paHelper(m - 1, i, atlantic, 0)
        ans = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) in atlantic:
                    ans.append([i, j])
        return ans