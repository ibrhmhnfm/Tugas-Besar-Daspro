import function
def initialize(array, r, column):
    i = 0
    while i in range (r):
        if array[i] == []:
            array[i] = [None]
            for j in range (column):
                if (j+1) in range (column):
                    array[i] = function.KonsDot(array[i],(j+1),None)
                else:
                    break
            if i != r:
                x = []
                array = function.KonsDot(array, (i+1), x)
        i += 1
    return array
def initialize_final(array, r):
    array = function.delfromarr([], array, r)
    return array
def initialize_username (username, users):
    b = 0
    while b < (102):
        if users[b] != [None, None, None]:
            username[b] = users[b][0]
            b += 1
        else:
            break
    return username