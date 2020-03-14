import heapq
from itertools import count


def huffman(seq, frq):
    counter = count()
    trees = list(zip(frq, counter, seq))
    heapq.heapify(trees)
    while len(trees) > 1:
        fa, __, a = heapq.heappop(trees)
        fb, __, b = heapq.heappop(trees)
        n = next(counter)
        # print(trees)
        heapq.heappush(trees, (fa + fb, n, [a, b]))
    return trees[0][-1]


if __name__ == '__main__':
    seq = "abcdefghi"
    frq = [4, 5, 6, 9, 11, 12, 15, 16, 20]
    res = huffman(seq, frq)
    print(res)
