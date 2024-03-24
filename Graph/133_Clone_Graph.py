"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        1. decide whether to use dfs or bfs: dfs
        2. use a HashMap to play as "visited" and store mappings
        3. use recursion to solve dfs (usually a helper function is needed)

        Time: O(n)
        Space: O(n)
        """
        mappings = {}

        def cloneHelper(n):
            if n in mappings:
                return mappings[n]
            mappings[n] = Node(n.val)
            # we don't know the exact data structure used to store neighbors
            # so I am not sure whether we can use list comprehension -> worked
            mappings[n].neighbors = [cloneHelper(nbr) for nbr in n.neighbors]
            return mappings[n]
        
        if not node:
            return None
        return cloneHelper(node)