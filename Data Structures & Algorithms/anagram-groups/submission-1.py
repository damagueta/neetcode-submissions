class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pilha = dict()

        for palavra in strs:
            sinalizador = "".join(sorted(palavra))
        
            if sinalizador not in pilha:
                pilha[sinalizador] = []
            
            pilha[sinalizador].append(palavra)

        return list(pilha.values())