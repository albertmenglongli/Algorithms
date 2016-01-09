import copy

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sum_array = copy.deepcopy(nums)
        for idx in range(1, len(self.sum_array)):
            self.sum_array[idx] += self.sum_array[idx - 1]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum_array[j] if i == 0 else self.sum_array[j] - self.sum_array[i - 1] 

def main():
    nums = [-2, 0, 3, -5, 2, -1]
    numArray = NumArray(nums)
    assert(numArray.sumRange(0, 2) == 1)
    assert(numArray.sumRange(2, 5) == -1)
    assert(numArray.sumRange(0, 5) == -3)

if __name__ == "__main__":
    main()
