"""There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?"""


class Solution(object):

    def candy(self, ratings):
        length = len(ratings)
        if length <= 1:
            return length
        # Each child must have at least one candy.
        results = [1 for _ in range(length)]
        for idx in range(1, length):
            if ratings[idx] > ratings[idx - 1]:
                results[idx] = results[idx - 1] + 1
        for idx in range(length - 1, 0, -1):
            if ratings[idx - 1] > ratings[idx]:
                results[idx - 1] = max(results[idx] + 1, results[idx - 1])
        return sum(results)

Solution().candy([2,1])