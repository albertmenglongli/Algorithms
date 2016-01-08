import numpy as np

def getBagMatrix(weights,values,pkgMaxCapacity):
    """
    This function generate bag matrix values like this,
    given :
            weights = [2, 2, 6, 5, 4]
            values = [6, 3, 5, 4, 6]
            pkgMaxCapacity = 10
    result:
            [[ 0  0  6  6  6  6  6  6  6  6  6]
             [ 0  0  6  6  9  9  9  9  9  9  9]
             [ 0  0  6  6  9  9  9  9 11 11 14]
             [ 0  0  6  6  9  9  9 10 11 13 14]
             [ 0  0  6  6  9  9 12 12 15 15 15]]
    """

    itemNums = len(weights)
    if not itemNums == len(values):
        raise Exception("Not right numbers of weights and values")
    bagMatrix = np.zeros(itemNums * (pkgMaxCapacity + 1), np.int).reshape(itemNums, pkgMaxCapacity + 1)
    for currPkgCapacity in range(1, pkgMaxCapacity + 1):
        for idx, (itemWeight, itemValue) in enumerate(zip(weights, values)):
            if currPkgCapacity < itemWeight:
                if idx > 0 :
                    bagMatrix[idx][currPkgCapacity] = bagMatrix[idx - 1][currPkgCapacity]
            else:
                if idx == 0 :
                    bagMatrix[idx][currPkgCapacity] = itemValue
                else:
                    bagMatrix[idx][currPkgCapacity] = max(bagMatrix[idx - 1][currPkgCapacity],
                                                          bagMatrix[idx - 1][currPkgCapacity - itemWeight] + itemValue)
    return bagMatrix

def main():
    weights = [2, 2, 6, 5, 4]
    values = [6, 3, 5, 4, 6]
    pkgMaxCapacity = 10
    bagMatrix = getBagMatrix(weights, values, pkgMaxCapacity)
    print bagMatrix[-1][-1]

if __name__ == "__main__":
    main()
