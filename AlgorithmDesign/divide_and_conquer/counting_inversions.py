from __future__ import print_function


def merge_and_count(seq):
    '''
    Counting the number of inversions in the sequence 2,4,1,3,5. Each crossing pair of line segments corresponds
    to one pair that is in the opposite order in the input list and the ascending list-in other words, an inversion.
    
    O(nlogn)

    2   4   1   3   5

    1   2   3   4   5

    # (2, 1), (4, 1), (4, 3)

    :param seq:
    :return: (number of inversions, inversion_pairs)
    '''

    from collections import deque

    def deque_split(d, nth):
        import itertools
        return deque(itertools.islice(d, nth)), deque(itertools.islice(d, nth, len(d)))

    def _merge_and_count(seq):
        mid = len(seq) // 2
        lft, rgt = deque_split(seq, mid)
        if len(lft) > 1: lft = _merge_and_count(lft)
        if len(rgt) > 1: rgt = _merge_and_count(rgt)
        result = []
        while lft and rgt:
            if lft[0] > rgt[0]:
                _merge_and_count.cnt += len(lft)
                for i in lft:
                    _merge_and_count.inversion_pair.append((i, rgt[0]))
                result.append(rgt.popleft())
            else:
                result.append(lft.popleft())

        return deque(result + (list(lft) + list(rgt)))

    _merge_and_count.cnt = 0
    _merge_and_count.inversion_pair = []
    _merge_and_count(seq)
    return _merge_and_count.cnt, _merge_and_count.inversion_pair


if __name__ == "__main__":
    print(merge_and_count(seq=[2, 4, 1, 3, 5]))
    # (3, [(2, 1), (4, 1), (4, 3)])
   
