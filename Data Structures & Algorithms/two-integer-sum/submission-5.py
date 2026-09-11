class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for idx, i in enumerate(nums):
            assinatura = target - i
            if assinatura in seen:
                return [seen[assinatura], idx]
            else:
                seen[i] = idx
        return False