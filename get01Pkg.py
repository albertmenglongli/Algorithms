import numpy as np

def getMaxValue(weights,values,pkgMaxCapacity):
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
    return bagMatrix[-1][-1] 
     
def main():
    weights = [2,2,6,5,4]
    values = [6,3,5,4,6]
    pkgMaxCapacity = 10
    print getMaxValue(weights, values, pkgMaxCapacity)

if __name__ == "__main__":
    main()
