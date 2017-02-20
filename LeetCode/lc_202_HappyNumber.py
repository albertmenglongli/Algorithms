class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def _inner(m, my_set):
            from math import pow
            if m == 1:
                return True
            lst_of_digs = []
            while m:
                v = m % 10
                lst_of_digs.append(v)
                m /= 10
            lst_of_digs.sort()
            tuple_of_digs = tuple(lst_of_digs)
            if tuple_of_digs in my_set:
                return False
            else:
                my_set.add(tuple_of_digs)
            next_value = sum(int(pow(e, 2)) for e in lst_of_digs)
            return _inner(next_value, my_set)

        return _inner(n, set())


assert Solution().isHappy(19)
assert not Solution().isHappy(18)
assert Solution().isHappy(10)
assert Solution().isHappy(1)
