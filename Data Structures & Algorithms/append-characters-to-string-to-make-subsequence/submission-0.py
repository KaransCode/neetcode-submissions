class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        i = j = 0

        while i < m and j < n:
            if s[i] != t[j]:
                i += 1
            else:
                i += 1
                j += 1
        return n - j