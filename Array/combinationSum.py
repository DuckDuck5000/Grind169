class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        
        output = []
        def helper(currPath, rem, start):
            
            if rem == 0:
                output.append(currPath)
            elif rem > 0:
                for i in range(start, len(candidates)):
                    currPath.append(candidates[i])
                    helper(currPath.copy(), rem - candidates[i], i)
                    currPath.pop()
            else:
                return 
        helper([], target, 0)
        return output