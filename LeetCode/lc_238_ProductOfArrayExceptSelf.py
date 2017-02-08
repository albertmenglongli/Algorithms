class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums or len(nums) < 2:
            return []

        print nums
        product_of_left_list = [1]
        for i in range(1, len(nums)):
            product_of_left_list.append(nums[i - 1] * product_of_left_list[i - 1])

        # actually we should also have a list named product_of_right_list
        # and multiply the two lists to get the final result
        # but to save memory, just reuse product_of_left_list
        output = product_of_left_list
        product_of_right_sofar = 1
        for i in range(len(nums) - 2, -1, -1):
            product_of_right_sofar *= nums[i + 1]
            output[i] *= product_of_right_sofar
        return output


if __name__ == "__main__":
    print Solution().productExceptSelf([1, 2, 3, 4])
