class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        from itertools import chain
        # step between each anchor,
        # anchor -- the indexes for the chars in first line,
        # including the one just act as a dummy anchor in the end
        step = numRows * 2 - 2
        anchors = [i * step for i in range(0, step + 1)]
        result = ''
        for i in range(numRows):
            # for each row, from top to down
            position_set = set(chain.from_iterable((anchor - i, anchor + i) for anchor in anchors))
            ordered_positions = sorted(filter(lambda x: 0 <= x < len(s), position_set))
            result += ''.join(s[idx] for idx in ordered_positions)
        return result

class Solution2:
    def convert(self, s, numRows):
        step = numRows * 2 - 2
        anchors = [i * step for i in range(0, step + 1)]
        result = ''

        # using a generator to avoid introducing itertools.chain
        def generate_positions(anchors, offset, start, end):
            for anchor in anchors:
                if start <= anchor - offset < end:
                    yield anchor - offset
                if start <= anchor + offset < end:
                    yield anchor + offset

        for i in range(numRows):
            positions_set = set(generate_positions(anchors, i, 0, len(s)))
            ordered_positions = sorted(positions_set)
            result += ''.join(s[idx] for idx in ordered_positions)
        return result


if __name__ == '__main__':
    assert Solution().convert("PAYPALISHIRING", 3) == 'PAHNAPLSIIGYIR'
    assert Solution().convert("PAYPALISHIRING", 4) == 'PINALSIGYAHRPI'
