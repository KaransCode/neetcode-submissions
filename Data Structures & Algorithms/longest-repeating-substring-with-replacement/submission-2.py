class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        maxFrequency = 0
        left = 0
        result = 0

        for right in range(len(s)):
            character = ord(s[right]) - ord('A')
            count[character] += 1
            maxFrequency = max(count[character], maxFrequency)
            
            window_size = right - left + 1
            if window_size - maxFrequency <= k:
                result = max(window_size, result)
            else:
                leftcharacter = ord(s[left]) - ord('A')
                count[leftcharacter] -= 1
                left += 1
        return result