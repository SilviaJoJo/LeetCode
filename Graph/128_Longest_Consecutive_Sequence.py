class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Similar to 200
        Time: O(n)
        Space: O(n)
        """
        if not nums:
            return 0
        n = len(nums)
        visited = set()
        ans = 1

        # when the input is in water: immediately returns
        # when the input is on island, but visited: immediately returns
        # when the input is on island and unvisited: get a whole island
        def bfs(i):
            # double-ended queue
            queue = collections.deque()
            queue.append(i)
            length = 1
            while queue:
                index = queue.popleft()
                visited.add(index)
                if index + 1 in range(n) and index + 1 not in visited:
                    if nums[index] + 1 == nums[index + 1]:
                        length += 1
                        queue.append(index + 1)
                    elif nums[index] == nums[index + 1]:
                        queue.append(index + 1)
                    
            return length

        nums.sort()
        for i in range(n):
            # again, add strict constraints to minimize calls
            if i not in visited and i + 1 < n and nums[i + 1] == nums[i] + 1:
                ans = max(ans, bfs(i))
        return ans