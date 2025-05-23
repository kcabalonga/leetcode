# Last updated: 5/23/2025, 1:48:35 AM
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        holder = [char for char in s if char in vowels]

        reversed = ""

        for char in s:
            if char in vowels:
                reversed += holder.pop()
            else:
                reversed += char

        return reversed

