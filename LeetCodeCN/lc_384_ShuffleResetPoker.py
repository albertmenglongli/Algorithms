from typing import List

from copy import deepcopy
from random import randrange


class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.array = deepcopy(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.array = deepcopy(self.original)
        return self.array

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.array)):
            tmp_idx = randrange(i, len(self.array))
            self.array[i], self.array[tmp_idx] = self.array[tmp_idx], self.array[i]
        return self.array

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
