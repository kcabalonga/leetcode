# Last updated: 5/23/2025, 1:06:25 AM
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max = 0
        result = []

        for candy in candies:
           if candy > max:
            max = candy

        for candy in candies:
            result.append(True if candy + extraCandies >= max else False)

        
        return result


