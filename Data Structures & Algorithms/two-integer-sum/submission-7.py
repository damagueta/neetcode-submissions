class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for idx, i in enumerate(nums):
            sinalizado = target - i
            if sinalizado in seen:
                return [seen[sinalizado], idx]
            else:
                seen[i] = idx