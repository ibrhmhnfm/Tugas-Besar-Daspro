def initialize(array, r, column):
    for i in range(r):
        if i >= r - len(array):
            array = KonsDot(array, i, [None] * column)
        elif not array[i]:
            array[i] = [None] * column
        else:
            for j in range(column - len(array[i])):
                array[i] = KonsDot(array, i, None)
    return array

def KonsDot(arr, r, x):
    arrnew = createarr(r + 1)
    for i in range(r):
        arrnew[i] = arr[i]
    arrnew[r] = x
    return arrnew

def createarr(r):
    arr = []
    for i in range(r):
        arr.append([])
    return arr

array = [[1,2,3],[2,3,4],[]]
print(initialize(array, 100, 3))
