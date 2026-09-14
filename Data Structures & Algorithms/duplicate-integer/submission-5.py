class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = dict()

        for idx, i in enumerate(nums):
            if i in seen:
                return True
            else:
                seen[i] = 1
        return False
            