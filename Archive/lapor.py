import function
#FUNGSIONAL YANG DIPERLUKAN
def hitung_pengumpul (users) :
    pengumpul=0
    for i in range(102) : 
        if users[i][2]=="pengumpul" :
            pengumpul+=1
    return pengumpul

def hitung_pembangun (users):
    pembangun=0
    for i in range(102) : 
        if users[i][2]=="pembangun" :
            pembangun+=1
    return pembangun

def username_pembangun(users, username):
    listnew = []
    j = 0
    for i in range (102):
        if users[i][2] == "pembangun":
            listnew = function.KonsDot(listnew,j,username[i])
            j +=1
    return (listnew, j)

def list_kerja(users, username, candi):
    (us_pembangun, r) = username_pembangun (users, username)
    listnew = [0 for i in range (r)]
    for i in range(r):
        for j in range (100):
            if (us_pembangun[i] == candi[j][1]):
                listnew[i] += 1
    return listnew

def hitung_rajin_malas (users, username, candi) : 
    (us_pembangun, r) = username_pembangun (users, username)
    arr_kerja = list_kerja(users, username, candi)
    if arr_kerja == [0 for i in range (r)] or r == 0:
        us_pembangun = ['-' for i in range (1)]
        idxmax = 0
        idxmin = 0
    else:
        idxmax = function.get_index(function.max_array(arr_kerja,r), arr_kerja, r)
        idxmin = function.get_index(function.min_array(arr_kerja,r), arr_kerja, r)
    return(us_pembangun[idxmax], us_pembangun[idxmin])

def laporjin(users, username, bahan_bangunan, candi):
    print(f"> Total Jin :{hitung_pembangun (users) + hitung_pengumpul (users)}")
    print(f"> Total Jin Pengumpul :{hitung_pengumpul (users)}")
    print(f"> Total Jin Pembangun :{hitung_pembangun (users)}")
    print(f"> Jin terajin :{hitung_rajin_malas(users, username, candi)[0]}")
    print(f"> Jin termalas :{hitung_rajin_malas(users, username, candi)[1]}")
    print(f"> Jumlah Pasir : {bahan_bangunan[0][2]} unit")
    print(f"> Jumlah air : {bahan_bangunan[1][2]} unit")
    print(f"> Jumlah Batu :{bahan_bangunan[2][2]} unit")


    