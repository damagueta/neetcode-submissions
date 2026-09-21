class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = dict()

        for palavra in strs:
            sinalizado = "".join(sorted(palavra))

            if sinalizado not in seen:
                seen[sinalizado] = []
            
            seen[sinalizado].append(palavra)

        resultado = list(seen.values())

        return resultado