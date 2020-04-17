def bisearch(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def bisect_right(nums, x):
    lo = 0
    hi = len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < nums[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo


def bisect_left(nums, x):
    lo = 0
    hi = len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if x > nums[mid]:
            lo = mid + 1
        else:
            hi = mid

    return lo


if __name__ == '__main__':
    nums = [1, 1, 4, 4, 7, 8, 10]
    print(bisearch(nums, 8))
    print(bisect_right(nums, 1))
    print(bisect_left(nums, 1))
    print(bisect_left(nums, 4))
