# Last updated: 5/28/2025, 3:49:39 AM
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                leftEmpty = (i == 0) or flowerbed[i - 1] == 0
                rightEmpty = (i == len(flowerbed) - 1) or flowerbed[i + 1] == 0
                if leftEmpty and rightEmpty:
                    flowerbed[i] = 1
                    n -= 1
        
        return n <= 0