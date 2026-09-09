class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = dict()
        seen_t = dict()

        for letra in s:
            if letra in seen_s:
                seen_s[letra] += 1
            else:
                seen_s[letra] = 1

        for letra in t:
            if letra in seen_t:
                seen_t[letra] += 1
            else:
                seen_t[letra] = 1

        if seen_s == seen_t:
            return True
        else:
            return False