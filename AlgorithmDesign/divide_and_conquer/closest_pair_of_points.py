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


def closest_pairs(points):
    def closest_pair_rec(points):
        # the input points is ordered by x-coordinate asc
        if len(points) <= 3:
            point_pair, min_value = None, float('inf')
            for p in points:
                for q in points[points.index(p) + 1:]:
                    if dis(p, q) < min_value:
                        min_value = dis(p, q)
                        point_pair = (p, q)
            return point_pair
        else:
            mid_idx = len(points) // 2

            left_points = sorted(points[mid_idx:], key=lambda p: p.x)
            right_points = sorted(points[:mid_idx], key=lambda p: p.x)

            (p1, p2) = closest_pair_rec(left_points)
            (q1, q2) = closest_pair_rec(right_points)

            point_pair, min_value = ((p1, p2), dis(p1, p2)) if dis(p1, p2) < dis(q1, q2) else ((q1, q2), dis(q1, q2))

            # here we make full use of the sorted points, order by x-coordinate
            leftmost_idx = mid_idx - 1
            rightmost_idx = mid_idx + 1
            while leftmost_idx >= 0 and abs(points[leftmost_idx].x - points[mid_idx].x) < min_value:
                if leftmost_idx == 0:
                    break
                leftmost_idx -= 1

            while rightmost_idx <= len(points) - 1 and abs(points[rightmost_idx].x - points[mid_idx].x) < min_value:
                if rightmost_idx == len(points) - 1:
                    break
                rightmost_idx += 1

            # points in middle, order by y-coordinate asc
            points_in_middle = sorted(points[leftmost_idx:rightmost_idx + 1], key=lambda p: p.y)
            for p in points_in_middle:
                # compare the current point p with the next following 15 points in y-coordinate asc order,
                # the value of 15 can be reduced, but it's an absolute constant
                for q in points_in_middle[points_in_middle.index(p) + 1: points_in_middle.index(p) + 16]:
                    if dis(p, q) < min_value:
                        min_value = dis(p, q)
                        point_pair = (p, q)
            return point_pair

    return closest_pair_rec(sorted([Point(x, y) for (x, y) in points], key=lambda p: p.x))


def main():
    closest_pair = closest_pairs([(0, 0), (7, 6), (2, 20), (12, 5), (16, 16), (5, 8), (19, 7), (14, 22), (8, 19), (7, 29), (10, 11), (1, 13)])
    print(closest_pair)
    # (Point(x=5, y=8), Point(x=7, y=6))


if __name__ == "__main__":
    main()
