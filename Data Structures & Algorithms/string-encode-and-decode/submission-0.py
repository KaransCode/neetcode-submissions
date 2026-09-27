class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        encoding = ""
        for word in strs:
            encoding = (str(len(word)) + "$")
            result += encoding + word
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        n = len(s)
        while i < n:
            j = i
            while s[j] != "$":
                j += 1
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            result.append(word)
            i = j + 1 + length
        return result
