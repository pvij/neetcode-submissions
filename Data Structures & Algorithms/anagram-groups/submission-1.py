from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        distinct_anagrams_dict = defaultdict(list)
        grouped_anagrams = []
        for word in strs:
            distinct_anagrams_dict[''.join(sorted(word))].append(word)

        return list(distinct_anagrams_dict.values())
        