class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grupos = dict()

        for palavra in strs:
            assinatura = "".join(sorted(palavra))

            if assinatura not in grupos:
                grupos[assinatura] = []

            grupos[assinatura].append(palavra)

        return list(grupos.values())
