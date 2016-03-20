if __name__ == "__main__":
    bad_table = [[0] * 5] * 5
    bad_table[0][1] = "bad"
    print bad_table
    # [[0, 'bad', 0, 0, 0], [0, 'bad', 0, 0, 0], [0, 'bad', 0, 0, 0], [0, 'bad', 0, 0, 0], [0, 'bad', 0, 0, 0]]

    table = [[0 for _ in range(5)] for _ in range(5)]
    table[0][0] = 1
    print table
    # [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
