class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        1. repeat the following process over all positions in the grid
            2. run bfs to find all positions for one island
            it returns when finished, with positions marked visited
                we use iteration (and queue) to realize bfs!
            3. increment the number of islands by 1
        4. return the number of islands

        Time: O(n^2) -- visited every node once
        Space: O(n^2)
        """
        m, n = len(grid), len(grid[0])
        visited = set()
        islands = 0

        # when the input is in water: immediately returns
        # when the input is on island, but visited: immediately returns
        # when the input is on island and unvisited: get a whole island
        def bfs(i, j):
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            # double-ended queue
            queue = collections.deque()
            queue.append((i, j))
            while queue:
                r, c = queue.popleft()
                # move the condition checking down inside the loop
                # so that every added element can be checked
                # which is different from dfs (iteration vs. recursion)
                if r in range(m) and c in range(n) and (r, c) not in visited and grid[r][c] == "1":
                    visited.add((r, c))
                    for dr, dc in directions:
                        queue.append((r + dr, c + dc))

        for i in range(m):
            for j in range(n):
                # this condition checking determines the number of islands
                if (i, j) not in visited and grid[i][j] == "1":
                    bfs(i, j)
                    islands += 1
        return islands
        