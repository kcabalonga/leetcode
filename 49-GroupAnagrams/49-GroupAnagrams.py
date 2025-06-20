# Last updated: 6/19/2025, 10:54:58 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for s in strs:
            anagrams[tuple(sorted(s))].append(s)
        
        return list(anagrams.values())
