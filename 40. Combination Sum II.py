"""Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, candidate_list, candidate_sum):
            if candidate_sum == target:
                res.append(candidate_list.copy())
                return
            if i >= len(candidates) or candidate_sum > target:
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j-1] == candidates[j]:
                    continue
                candidate_list.append(candidates[j])
                candidate_sum += candidates[j]
                backtrack(j+1, candidate_list, candidate_sum)
                candidate_list.pop()
                candidate_sum -= candidates[j]
        backtrack(0, [], 0)
        return res
