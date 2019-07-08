class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        head, tail = 0, len(nums) - 1
        while head < tail:
            sum = sorted_nums[head] + sorted_nums[tail]
            if sum == target:
                break
            elif sum > target:
                tail -= 1
            else:
                head += 1
        first_idx,  second_idx = nums.index(sorted_nums[head]), nums.index(sorted_nums[tail])
        if first_idx == second_idx:
            second_idx = nums.index(sorted_nums[tail], second_idx + 1)
        return [first_idx,  second_idx]


def main():
    print(Solution().twoSum(nums=[0,4,3,0], target=0))

if __name__ == '__main__':
    main()
