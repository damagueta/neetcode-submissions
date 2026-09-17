class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        guardar = dict()

        for idx, i in enumerate(nums):
            alvo = target - i

            if alvo in guardar:
                return [guardar[alvo], idx]
            
            guardar[i] = idx


