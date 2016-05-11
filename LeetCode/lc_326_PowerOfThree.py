def isPowerOfN(n, num, step = 0):
    result = pow(n, step)
    if result == num:
        return True
    elif result > num:
        return False
    elif result < num:
        return isPowerOfN(n, num, step + 1)

def main():
    inputs = [-1, 1, 3, 4, 12, 14, 27, 64, 81, 84, 132]
    print zip(inputs, map(lambda x : isPowerOfN(2, x), inputs))
    # [(-1, False), (1, True), (3, False), (4, True), (12, False), (14, False), (27, False), (64, True), (81, False), (84, False), (132, False)]
    print zip(inputs, map(lambda x : isPowerOfN(3, x), inputs))
    # [(-1, False), (1, True), (3, True), (12, False), (14, False), (27, True), (81, True), (84, False), (132, False)]

if __name__ == "__main__":
    main()
