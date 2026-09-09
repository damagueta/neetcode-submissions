class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        contador = dict()

        for i in nums:
            if i in contador:
                contador[i] += 1
            else:
                contador[i] = 1

        frequencia = sorted(contador, key=lambda n: contador[n], reverse=True)
        return frequencia[:k]
        