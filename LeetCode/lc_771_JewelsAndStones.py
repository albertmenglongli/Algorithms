class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        from collections import Counter
        return sum(Counter({k: v for k, v in Counter(S).items() if k in J}).values())


if __name__ == "__main__":
    J = "aA"
    S = "aAAbbbb"

    print(Solution().numJewelsInStones(J, S))
    