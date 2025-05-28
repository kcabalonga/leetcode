# Last updated: 5/28/2025, 3:49:19 AM
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


