from typing import List


def is_axis_overlap(m1, m2, n1, n2):
    # assuming m1 < m2, n1 < n2
    if m1 >= n2 or m2 <= n1:
        return False
    else:
        return True


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        xp1, yp1, xp2, yp2 = rec2
        return is_axis_overlap(x1, x2, xp1, xp2) and is_axis_overlap(y1, y2, yp1, yp2)
