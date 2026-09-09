class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i in range(len(nums)):
            complemento = target - nums[i]

            if complemento in seen:
                return [seen[complemento], i]
            else:
                seen[nums[i]] = i 