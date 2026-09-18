class Solution:
    def scoreOfString(self, s: str) -> int:
        scores = []
        result = 0
        for char in s:
            score = ord(char)
            scores.append(score)
            
        for i in range(1,len(scores)):
            result += abs(scores[i] - scores[i-1])
        return result