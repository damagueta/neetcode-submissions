class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = dict()

        for palavra in strs:
            sinalizador = "".join(sorted(palavra))
            
            if sinalizador not in seen:
                seen[sinalizador] = []

            seen[sinalizador].append(palavra)

        resultado = list(seen.values())
        
        return resultado

