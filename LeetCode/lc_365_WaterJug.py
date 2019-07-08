class Solution:
    def canMeasureWater(self, x, y, z):
        if z == 0:
            return True
        if x == 0 or y == 0:
            return False
        max = x + y
        if x < y:
            x, y = y, x
        while y:
            temp = x % y
            x = y
            y = temp

        return True if z % x == 0 and z <= max else False


print(Solution().canMeasureWater(6, 9, 300))
