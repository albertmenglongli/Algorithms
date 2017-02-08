# -*- coding:utf-8 -*-

# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).
# You begin the journey with an empty tank at one of the gas stations.
# Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
# Note:
# The solution is guaranteed to be unique.



class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        from itertools import imap
        if not gas or not cost or not (len(gas) == len(cost)):
            return -1
        my_diff = list(imap(lambda m, n: m - n, gas, cost))
        n = len(gas)

        start = 0
        while start < n:
            if my_diff[start] < 0:
                start += 1
                continue
            else:
                break

        if start != n:
            sofar_max = my_diff[start]
        else:
            sofar_max = 0
        for i in range(start + 1, 2 * n):

            if start >= n:
                return -1
            while start <= i:
                if sofar_max >= 0:
                    break
                else:
                    sofar_max -= my_diff[start]
                    start += 1
                continue

            if i - start == n and sofar_max >= 0:
                return start
            idx = i
            if i >= n:
                idx = idx % n
            sofar_max += my_diff[idx]

        return -1


def main():
    gas = [2,4]
    cost = [3,4]
    print Solution().canCompleteCircuit(gas=gas, cost=cost)


if __name__ == '__main__':
    main()
