def createarr(a, z):
    arr = [0 for i in range (a,z)]
    return arr
def Konso (x, list, r):
    listnew = [0 for i in range (r+1)]
    for i in range (1,r):
        listnew[i] = list[i-1]
    listnew[0] = x
    return listnew
def KonsDot (list, r, x):
    listnew = [ 0 for i in range (r+1)]
    for i in range (0,r):
        listnew[i] = list[i]
    listnew[r] = x
    return listnew
def sumlist (list, r):
    suml = 0
    for i in range(r):
        suml += list[i]
    return suml
def inlist (x, list, r):
    inside = False
    for i in range (r):
        if x == list[i]:
            inside = True
    return inside
def delso (list, r):
    listnew = [0 for i in range (r-1)]
    for i in range (r-1):
        listnew[i] = list[i+1]
    return listnew
def delsdot (list, r):
    listnew = [0 for i in range (r-1)]
    for i in range (r-1):
        listnew[i] = list[i]
    return listnew
def delfl1 (x, list, r):
    for i in range (r):
        if x == list[i]:
            for j in range(i,r):
                if j+1 in range(r):
                    temp = list[j+1]
                    list[j] = temp
                else:
                    break
    return delsdot(list, r)
def delfromlist (x, list, r):
    while inlist(x, list, r):
        list = delfl1 (x, list, r)
        r -= 1
    return list

            



