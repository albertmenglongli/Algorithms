from __future__ import print_function


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dis(self, other):
        import math
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __repr__(self):
        return 'Point(x=%s, y=%s)' % (self.x, self.y)

    def __eq__(self, other):
        return self is other or isinstance(other, Point) and self.x == other.x and self.y == other.y


def distance_calculation_memoize(function):
    memo = {}

    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            # for distance calculation, the result for dis(p1, p2) is the same as dis(P2, p1)
            memo[(args[1], args[0])] = rv
            return rv

    return wrapper


@distance_calculation_memoize
def dis(p1, p2):
    return p1.dis(p2)


def bisect_left(lst, x, lo=0, hi=None, key=lambda x: x):
    """Return the index where to insert item x in list a, assuming a is sorted.

       The return value i is such that all e in a[:i] have e < x, and all e in
       a[i:] have e >= x.  So if x already appears in the list, a.insert(x) will
       insert just before the leftmost x already there.

       Optional args lo (default 0) and hi (default len(a)) bound the
       slice of a to be searched.
    """
    assert lo >= 0, "low must be non-negative"
    hi = hi or len(lst)

    x_key = key(x)
    while lo < hi:
        mid = (lo + hi) // 2
        if x_key > key(lst[mid]):
            lo = mid + 1
        else:
            hi = mid
    return lo


def closest_pair(points):
    def closest_pair_rec(points):
        # the input points is ordered by x-coordinate asc
        if len(points) <= 3:
            pair_of_points, min_value = None, float('inf')
            for p in points:
                for q in points[points.index(p) + 1:]:
                    if dis(p, q) < min_value:
                        min_value = dis(p, q)
                        pair_of_points = (p, q)
            return pair_of_points
        else:
            mid_idx = len(points) // 2

            # partition the points into left and right parts, both parts are ordered by x-coordinate
            left_points = sorted(points[mid_idx:], key=lambda p: p.x)
            right_points = sorted(points[:mid_idx], key=lambda p: p.x)

            # calculate the closest pair of points in each part separately
            (p1, p2) = closest_pair_rec(left_points)
            (q1, q2) = closest_pair_rec(right_points)

            pair_of_points, min_value = ((p1, p2), dis(p1, p2)) if dis(p1, p2) < dis(q1, q2) else ((q1, q2), dis(q1, q2))

            # find the leftmost and rightmost points indexes within the middle part, with width of 2 * min_value, each min_value for each part
            # taking advantage of the sorted points ordered by x-coordinate
            # using customized bisect due to the build-in bisect do not support comparison key, the second parameter is temporary Point if I wanna insert.
            leftmost_idx = bisect_left(points, Point(points[mid_idx].x - min_value, 0), 0, mid_idx, lambda p: p.x)
            rightmost_idx = bisect_left(points, Point(points[mid_idx].x + min_value, 0), mid_idx, key=lambda p: p.x)

            # points in middle section, ordered in y-coordinate asc
            middle_points = sorted(points[leftmost_idx:rightmost_idx + 1], key=lambda p: p.y)
            for p in middle_points:
                # compare the current point p with the next following 15 points in y-coordinate asc order,
                # the value of 15 can be reduced, but it's an absolute constant
                for q in middle_points[middle_points.index(p) + 1: middle_points.index(p) + 16]:
                    if dis(p, q) < min_value:
                        min_value = dis(p, q)
                        pair_of_points = (p, q)
            return pair_of_points

    return closest_pair_rec(sorted([Point(x, y) for (x, y) in points], key=lambda p: p.x))


def main():
    # in this algorithm, we assume that there's no two points having the same x-coordinate or y-coordinate
    points = [(0, 0), (7, 6), (2, 20), (12, 5), (16, 16), (5, 8), (19, 7), (14, 22), (8, 19), (7, 29), (10, 11), (1, 13)]
    print(closest_pair(points))
    # (Point(x=5, y=8), Point(x=7, y=6))


if __name__ == "__main__":
    main()
