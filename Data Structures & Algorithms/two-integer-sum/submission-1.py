class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if i == j:
                    pass
                else:
                    soma = nums[i] + nums[j]
                if soma == target:
                    return [i,j]
        return False