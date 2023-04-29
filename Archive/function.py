# Butuh : masi belum bikin parser
# kl bikin fungsi baru, kasi komen buat ganti apa, biar g dobel
# edit aj kl rasany fungsi kurang bagus/g sesuai, tp tambahin komen digantiny apa
def createarr(a): #Buat bikin gampang inisialisasi array
    arr = [0 for i in range (a)]
    return arr
def createarrstr(a):
    arrstr = [None for i in range (a)]
    return arrstr
# x : yg mau dimasukin, arr : array tujuan x, r : panjang array (harusny statis, jadi diketahui.)
def Konso (x, arr, r): # Menambah x ke array, x di depan. Return berupa array (ganti .append())
    arrnew = createarr(r+1)
    for i in range (1,r):
        arrnew[i] = arr[i-1]
    arrnew[0] = x
    return arrnew
# x : yg mau dimasukin, arr : list tujuan x, r : panjang list
def KonsDot (arr, r, x):  # Menambah x ke list, x di belakang. Return berupa list (ganti .append())
    arrnew = createarr(r+1)
    for i in range (0,r):
        arrnew[i] = arr[i]
    arrnew[r] = x
    return arrnew
# list : list yang mau ditambahin elemennya, r : panjang list 
def sumarr (arr, r): # Jumlah semua dalam list (ganti .sum())
    suml = 0
    for i in range(r):
        suml += arr[i]
    return suml
# x : elemen yg mau dicari ada atau engg nya, list: list yang dicek, r : panjang list
def inlist (x, arr, r): # Menentuin ada elemen di list atau engg. True kl ada, False kl engg. (ganti 'in')
    inside = False
    for i in range (r):
        if x == arr[i]:
            inside = True
    return inside
def delso (arr, r): # fungsi buat ngehapus elemen pertama (memperpendek list)
    arrnew = createarr(r-1)
    for i in range (r-1):
        arrnew[i] = arr[i+1]
    return arrnew
def delsdot (arr, r): # fungsi buat menghapus elemen terakhir (memperpendek list)
    arrnew = createarr(r-1)
    for i in range (r-1):
        arrnew[i] = arr[i]
    return arrnew
def delfl1 (x, arr, r): # fungsi buat delfromlist, menukar nilai x yg pertama kali ditemukan ke belakang list
    for i in range (r):
        if x == arr[i]:
            for j in range(i,r):
                if j+1 in range(r):
                    temp = arr[j+1]
                    arr[j] = temp
                else:
                    break
    return delsdot(arr, r)
def delfromarr (x, arr, r): # fungsi buat menghapus semua nilai x di list (ganti .pop())
    while inlist(x, arr, r):
        arr = delfl1 (x, arr, r)
        r -= 1
    return arr
def slicefront (arr, i): # gantiin arr[:i]
    arrnew = createarr(i)
    for j in range (i):
        arrnew[j] = arr[j]
    return arrnew
def sliceback (arr, a, r): # gantiin arr[i:]
    arrnew = createarr(r-a)
    for i in range (a, r):
        j = i - a
        arrnew[j] = arr[i]
    return arrnew
def sort (arr, r): # pengganti sorted()
    switch = False
    for i in range(r-1):
        for j in range(0, r-i-1):
            if arr[j] > arr[j+1]:
                switch = True
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        if not switch:
            break
    return arr
def get_index (x, arr, r): # ganti .index()
    index = None
    for i in range (r):
        if x == arr[i]:
            index = i
            break
    return index
def joinwords (arrstr): # fungsi buat nambahin array of char jadi kata
    word = ''
    for i in range (len(arrstr)): # len boleh utk string
        word += arrstr[i]
    return word
def split (li, banyak, str): # ganti .split()
    r = len(li) # len boleh u/ string
    listnew = createarr(banyak)
    for i in range (banyak):
        a = get_index(str, li, r)
        if inlist(str, li, r):
            if a == 0:
                li = delso (li, r)
                r -= 1
                a = get_index(str, li, r)
            listnew1 = slicefront(li, a)
            li = sliceback(li, a, r)
            li = delso (li, (r-a))
            r -= (a+1)
            listnew[i] = joinwords(listnew1)
            if r > 0 and not inlist (str, li, r):
                listnew[i+1] = joinwords(li)
        else:
            break
    return listnew
def max_array(arr, r):
    max = 0
    for i in range(r):
        if arr[i] > max:
            max = arr[i]
    return max


def min_array(arr, r):
    min = 100000000
    for i in range(r):
        if arr[i] < min:
            min = arr[i]
    return min

# Parser
def open_csv (csv):
    listnew = createarrstr()

#Absolute
def absolute (int):
    if int < 0:
        int = 0 - int
    return int

# Replace All
# mengembalikan array baru dengan elemen pada index yang ditentukan telah dihapus
# (pengganti keyword del)
def del_by_index(li, index, length):
  # li adalah list yang elemennya mau dihapus
  # index adalah index posisi elemen yang mau dihapus
  # length adalah panjang list yang elemennya mau dihapus
  arr = createarr(length-1)
  indeksarr = 0
  for i in range(length):
    if i != index:
      arr[indeksarr] = li[i]
      indeksarr += 1
  return arr