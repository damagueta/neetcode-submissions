class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = dict()

        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        
        resultado = list(sorted(seen, reverse=True, key=lambda x: seen[x]))

        return resultado[:k]