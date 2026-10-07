class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
    
        for idx, i in enumerate(nums):
            sinal = target - i
            if sinal in seen:
                return [seen[sinal], idx]
            seen[i] = idx
        return False