# Last updated: 5/28/2025, 3:46:04 AM
class Solution:
    def reverseWords(self, s: str) -> str:
        reverse = s.split()[::-1]
        return " ".join(reverse)
