# Last updated: 5/20/2025, 6:12:15 PM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        merged = ""
        while i < max(len(word1), len(word2)):
            if i < len(word1):
                merged += word1[i]
            if i < len(word2):
                merged += word2[i]
            i += 1

        return merged
