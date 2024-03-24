class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        1. there are 3 representations of a graph, and the one provided is edge set
        2. convert edge set to adjacency list (another representation)
        3. have a set as visited
        4. use dfs and a helper function
        5. consider edge cases: not fully connected graph

        Time: O(n + m)
        Space: O(n + m)
        """
        # list comprehension can be adapted for map
        pres = {i : [] for i in range(numCourses)}
        for prerequisite in prerequisites:
            pres[prerequisite[0]].append(prerequisite[1])
        visited = set()

        def cfHelper(n):
            # Base case 1: a circle -> impossible
            if n in visited:
                return False
            # Base case 2: no prerequisite
            elif not pres[n]:
                return True
            visited.add(n)
            for pre in pres[n]:
                if not cfHelper(pre):
                    return False
        # the trick here is that, when a prerequisite is visited and marked true
        # it will still be marked as false in later recursion
        # so we should delete it from visited, and mark it as true
            pres[n] = []
            visited.remove(n)
            return True
        
        for i in range(numCourses):
            if not cfHelper(i):
                return False
        return True