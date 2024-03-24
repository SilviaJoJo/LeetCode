class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        1. to avoid duplicates (of same elements, same frequency)
            we should consider subproblems like this:
            2. use the current element: further recursion
            3. do not use the current element: further recursion
        2. yes for this problem we have to do recursion
        
        Time: O(2^target) -- tree structure, worst case height target
        Space: O(2^target) -- all leaf nodes will be stored in the worst case
        """
        ans = []
        # dfs -> go into every possible route
        # total vs. target -> tail recursion
        def combinationHelper(i, currList, total):
            # Base case 1: successful
            if total == target:
                ans.append(currList)
            # Base case 2: unsuccessful -> used up all elements or exceed target
            elif i >= len(candidates) or total > target:
                return
            else:
                # subproblem 1: use the ith element
                combinationHelper(i, currList + [candidates[i]], total + candidates[i])
                # subproblem 2: do not use the ith element
                combinationHelper(i + 1, currList, total)
            
        combinationHelper(0, [], 0)
        return ans