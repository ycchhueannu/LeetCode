class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        if len(flowerbed) == 1:
            if not flowerbed[0]:
                return True
            return False
        
        if not flowerbed[0] and not flowerbed[1]:
            flowerbed[0] = 1
            n -= 1
        for i in range(1, len(flowerbed)-1):
            if not flowerbed[i] and not flowerbed[i-1] and not flowerbed[i+1]:
                flowerbed[i] = 1
                n -= 1
                if n <= 0:
                    return True
        if not flowerbed[-1] and not flowerbed[-2]:
            flowerbed[-1] = 1
            n -= 1

        return n <= 0