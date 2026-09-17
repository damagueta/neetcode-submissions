class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lista = dict()

        for i in nums:
            if i in lista:
                return True
            else:
                lista[i] = "çalskfdjçaslk"
        
        return False