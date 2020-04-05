def get_min_k(arr, k):
    def partition(s, t):
        pivot = arr[s]
        i = s
        for j in range(s + 1, t + 1):
            if arr[j] < pivot:
                arr[j], arr[i + 1] = arr[i + 1], arr[j]
                i += 1
        arr[s], arr[i] = arr[i], arr[s]
        return i

    if not arr or len(arr) < k or k <= 0:
        return None

    s, t = 0, len(arr) - 1

    while True:
        idx = partition(s, t)

        if idx == k - 1:
            return arr[idx]
        elif idx > k - 1:
            t = idx - 1
        else:
            s = idx + 1


if __name__ == '__main__':
    arr = [2, 3, 4, 1, 5, 10, 9, 7, 8, 6]
    assert get_min_k(arr, 3) == 3
    assert get_min_k(arr, 4) == 4
    assert get_min_k(arr, 10) == 10
