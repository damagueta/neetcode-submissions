class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = dict()

        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        
        resultado = sorted(seen, key=lambda n: seen[n], reverse=True)
        return resultado[:k]
