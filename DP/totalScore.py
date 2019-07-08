class Solution(object):

    def f(self, n):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            return self.f(n - 3) + self.f(n - 5) + self.f(n - 10)

    def f_memo(self, n):
        array = [0] * (n + 1)

        def _f(n):
            if n < 0:
                return 0
            elif n == 0:
                return 1
            if not array[n]:
                array[n] = _f(n - 3) + _f(n - 5) + _f(n - 10)
            return array[n]

        res = _f(n)
        # if n = 13:
        # array used for memo looks like
        # [0, 0, 0, 1, 0, 1, 0, 0, 2, 0, 2, 0, 0, 5]
        return res

    def f_bottom_up_dp(self, n):
        m = max(n, 10)
        array = [0] * (m + 1)
        # for score 0, there's only 1 case: 0
        array[0] = 1
        array[3] = array[5] = array[10] = 1
        for i in range(1, n + 1):
            array[i] += array[i - 3] if i - 3 > 0 else 0
            array[i] += array[i - 5] if i - 5 > 0 else 0
            array[i] += array[i - 10] if i - 10 > 0 else 0
        # if n = 13:
        # array looks like
        # [0, 0, 0, 1, 0, 1, 1, 0, 2, 1, 2, 3, 1, 5]
        return array[n]


print(Solution().f(13))
print(Solution().f_memo(13))
print(Solution().f_bottom_up_dp(13))
