class Solution(object):

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.results = []
        self.candidates = candidates
        self.target = target
        self._combination(len(candidates) - 1, [])
        return self.results

    def _combination(self, idx, result):
        from copy import deepcopy
        remain = self.target - sum(result)
        if remain == 0:
            return self.results.append(deepcopy(result))
        if idx >= 0:
            ele = self.candidates[idx]
            for i in range(remain / ele + 1):
                result.extend([ele] * i)
                self._combination(idx - 1, result)
                result = filter(lambda x: x != ele, result)

print Solution().combinationSum(candidates=[2, 3, 6, 7], target=7)
