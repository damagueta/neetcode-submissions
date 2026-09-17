class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        visto_s = dict()
        visto_t = dict()

        for letra in s:
            if letra in visto_s:
                visto_s[letra] += 1
            else:
                visto_s[letra] = 1

        for letra in t:
            if letra in visto_t:
                visto_t[letra] += 1
            else:
                visto_t[letra] = 1

        if visto_s == visto_t:
            return True
        else:
            return False
