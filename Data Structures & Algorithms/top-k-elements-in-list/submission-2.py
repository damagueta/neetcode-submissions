class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        contagem = dict()

        for i in nums:
            if i in contagem:
                contagem[i] += 1
            else:
                contagem[i] = 1

        resultado = sorted(contagem, reverse=True, key=lambda x: contagem[x])
        return resultado[:k]