class Solution(object):
    @staticmethod
    def countBits(num):
        """
        :type num: int
        :rtype: List[int]
        >>> Solution.countBits(5)
        [0, 1, 1, 2, 1, 2]
        """
        init_lst = [0]
        cnt = len(init_lst)
        while cnt < num + 1:
            init_lst = init_lst + [e + 1 for e in init_lst]
            cnt *= 2
        return init_lst[0: num + 1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
