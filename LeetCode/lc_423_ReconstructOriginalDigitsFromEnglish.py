# -*- coding:utf-8 -*-
from collections import Counter
from copy import deepcopy


class Solution(object):
    def __init__(self):
        self.results = []

    digit_letter_mapping = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }

    my_dict = {k: Counter(v) for k, v in digit_letter_mapping.items()}

    def dfs(self, s_counter, result):
        if self.results:
            return
        if all(s_counter[character] == 0 for character in s_counter.keys()):
            self.results.append(deepcopy(result))
        for k, v in self.my_dict.items():
            count = 0
            while all(s_counter[character] >= v[character] * (count + 1) for character in v.keys()):
                count += 1
            if count:
                for v_k, v_v in v.items():
                    s_counter[v_k] -= v_v * count
                result.extend([k] * count)

                self.dfs(s_counter, result)
                for v_k, v_v in v.items():
                    s_counter[v_k] += v_v * count

                while count:
                    result.pop()
                    count -= 1

    def originalDigits(self, s):
        s_counter = Counter(s)
        self.dfs(s_counter, [])
        # assuming there's only one result
        self.results[0].sort()
        return "".join([str(e) for e in self.results[0]])


class Solution2:
    digit_letter_mapping = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }

    my_dict = {k: Counter(v) for k, v in digit_letter_mapping.items()}

    def originalDigits(self, s):
        import string
        import numpy as np
        from collections import Iterable
        from collections import OrderedDict
        s_counter = Counter(s)

        letter_freq = OrderedDict()
        for dig in range(0, 10):
            letter_freq[dig] = [Counter(self.digit_letter_mapping[dig]).get(e, 0) for e in string.ascii_lowercase]
        a = np.array([v for k, v in letter_freq.items()])
        a = a.transpose()
        b = np.array([s_counter.get(e, 0) for e in string.ascii_lowercase])
        # 利用多元一次不定方程进行求解
        x = np.linalg.lstsq(a, b)
        results = []
        # 移除掉其他的非整数解，只保留整数解，完整的流程应该是仅保留正整数解
        for r in x:
            if not isinstance(r, Iterable):
                continue
            if all(abs(round(e) - e) < 0.001 for e in r) and len(r) == 10:
                results.append([int(round(e)) for e in r])

        result = results[0]
        return ''.join([str(idx) * val for idx, val in enumerate(result)])


def main():
    print(Solution().originalDigits("fviefuro"))
    print(Solution().originalDigits("zeroonetwothreefourfivesixseveneightnine"))

    s1 = "fviefuro"
    print(s1)
    print(Solution2().originalDigits(s1))
    s2 = "zeroonetwothreefourfivesixseveneightnine"
    print(s2)
    print(Solution2().originalDigits(s2))


if __name__ == '__main__':
    main()
