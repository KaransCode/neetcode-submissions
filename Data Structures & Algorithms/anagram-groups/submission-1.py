from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)
        for string in strs:
            count = [0]*26
            for word in string:
                char = (ord(word)-ord('a'))
                count[char] += 1
            count = tuple(count)
            dictionary[count].append(string)
        anagrams = list(dictionary.values())
        return anagrams