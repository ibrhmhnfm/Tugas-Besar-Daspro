import function
from function import KonsDot
from function import get_index

#[[id,Pembuat,pasir,batu,air]]
sum=0

def lapor_jumlah_candi (candi):
    hitung = 0
    i = 0
    while i < 100:
        if candi[i] != [None, None, None, None, None]:
            hitung += 1
            i += 1
        else:
            hitung += 0
            i += 1
    return hitung

def lapor_jumlah_bahan (candi, a):
    jumlah_pasir = 0
    jumlah_batu = 0
    jumlah_air = 0
    i = 0
    while i < 100:
        if candi[i] != [None, None, None, None, None]:
            jumlah_pasir += int(candi[i][2])
            jumlah_batu += int(candi[i][3])
            jumlah_air += int(candi[i][4])
            i += 1
        else:
            i += 1
    arr = [jumlah_pasir, jumlah_batu, jumlah_air]
    return arr[a]

def harga (candi):
    harga =[]
    i = 0
    while i < 100 :
        if candi[i] != [None, None, None, None, None]:
            sum_harga=int(candi[i][2])*10000+int(candi[i][3])*15000+int(candi[i][4])*7500
            harga = KonsDot(harga, i, sum_harga)
            i += 1
        else:
            harga = KonsDot(harga, i, 0)
            i += 1
    return harga

def lapor_candi_mahal (candi) : 
    max = function.max_array(harga(candi), 100)
    return max

def min_array_harga (array, r):
    min = 999999
    for i in range (r):
        if array[i] < min and array[i] != 0:
            min = array[i]
        else:
            min = min
    return min

def lapor_candi_murah (candi) :
    min = min_array_harga(harga(candi), 100)
    return min

def lapor_id_mahal(candi):
    idx = get_index(lapor_candi_mahal(candi), harga (candi), 100)
    idx +=1
    return idx

def lapor_id_murah(candi):
    idx = get_index(lapor_candi_murah(candi), harga(candi), 100)
    idx +=1
    return idx


#PROGRAM UTAMA
def laporan_candi(candi):
    print(f"> Total Candi: {lapor_jumlah_candi(candi)}")
    print(f"> Total Pasir yang digunakan: {lapor_jumlah_bahan(candi, 0)}")
    print(f"> Total Batu yang digunakan: {lapor_jumlah_bahan(candi, 1)}")
    print(f"> Total Air yang digunakan:{lapor_jumlah_bahan(candi, 2)}")
    print(f"> ID Candi Termahal: {lapor_id_mahal(candi)} (Rp {lapor_candi_mahal(candi)})")
    print(f"> ID Candi Termurah: {lapor_id_murah(candi)} (Rp {lapor_candi_murah(candi)})")