class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = dict()

        for i in strs:
            sinal = "".join(sorted(i))

            if sinal not in seen:
                seen[sinal] = []
            
            seen[sinal].append(i)

        
        resultado = list(seen.values())

        return resultado