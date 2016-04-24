class Solution(object):

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        init_lst = [0]
        cnt = len(init_lst)
        while cnt < num + 1:
            init_lst = init_lst + [e + 1 for e in init_lst]
            cnt *= 2
        return init_lst[0: num + 1]

if __name__ == "__main__":
    print Solution().countBits(5)
    # >> [0, 1, 1, 2, 1, 2]
