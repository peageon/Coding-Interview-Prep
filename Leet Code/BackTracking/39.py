#Combination Sum
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        sol = []
        temp = []

        def dfs(ind, tar):
            for candidate_ind in range(ind,len(candidates)):
                if candidates[candidate_ind] < tar:
                    temp.append(candidates[candidate_ind])
                    dfs(candidate_ind, tar-candidates[candidate_ind])
                    temp.pop()
                elif candidates[candidate_ind] == tar:
                    temp.append(candidates[candidate_ind])
                    sol.append(temp.copy())
                    temp.pop()
                    return
                elif candidates[candidate_ind] > tar:
                    return
        
        dfs(0, target)
        return sol