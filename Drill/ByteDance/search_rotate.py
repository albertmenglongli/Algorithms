arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]


def search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > arr[left]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

        if arr[mid] < arr[right]:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def find_rotate_index(nums):
    left = 0
    right = len(nums) - 1
    if nums[left] < nums[right]:
        return 0

    while left < right:
        pivot = (left + right) // 2
        if nums[right] < nums[pivot]:
            left = pivot + 1
        else:
            right = pivot
    return left


if __name__ == '__main__':
    assert search(arr, 15) == 0
    assert search(arr, 16) == 1
    assert search(arr, 19) == 2
    assert search(arr, 20) == 3
    assert search(arr, 25) == 4
    assert search(arr, 1) == 5
    assert search(arr, 3) == 6
    assert search(arr, 4) == 7

    assert find_rotate_index(arr) == 5
