class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = dict()

        for idx, i in enumerate(strs):
            sinalizado = "".join(sorted(i))

            if sinalizado not in seen:
                seen[sinalizado] = []

            seen[sinalizado].append(i)

        resultado = list(seen.values())

        return resultado