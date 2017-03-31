'''
             i-2
    case 1 : i-1┌─┐
                └─┼─>i
                 i-3

                    i-2
    case 2 : i-1 ┌────┐
                 └─══>┘i-3
                 i  i-4      (i overlapped i-4)

    case 3 :    i-4
               ┌──┐
               │i<┼─┐
            i-3│ i-5│i-1
               └────┘
                i-2

'''


class Solution(object):
    def isSelfCrossing(self, x):
        b = c = d = e = f = 0
        for a in x:
            if d >= b > 0 and (a >= c or a >= c - e >= 0 and f + b >= d):
                return True
            b, c, d, e, f = a, b, c, d, e
        return False
