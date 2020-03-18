def get_max_subarray(lst):
    if not lst:
        return []
    sofar = lst[0]
    result = -float('inf')

    for i in range(1, len(lst)):
        curr = lst[i]
        # 对于每一个元素：判断sofar与当前值的关系，来决定是否继续继承之前的sofar，还是以当前元素重新立sofar
        # 一、sofar: 最大的子序列包含之前+当前；
        # 二、sofar: 放弃之前，从当前元素开始重新算（发生在之前的序列之和为负）；
        sofar = max(sofar + curr, curr)

        if sofar > result:
            result = sofar

    return result


if __name__ == '__main__':
    lst = [1, -2, 3, 10, -4, 7, 2, -5]
    print(get_max_subarray(lst))

