# Last updated: 6/19/2025, 10:47:15 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxLength = 0

        i = 0
        j = 0

        while i < len(s):
            if s[i] not in seen:
                seen.add(s[i])
                i += 1
            else:
                seen.remove(s[j])
                j += 1
            maxLength = max(maxLength, i - j)
        
        return maxLength