#FUNGSIONAL YANG DIPERLUKAN
from random import randint
def hitung_pengumpul (users) :
    pengumpul=0
    for i in range(102) : 
        if users[i][2]=="pengumpul" :
            pengumpul+=1
    return pengumpul
def hitung_pasir() :
    pasir=0
    pasir+= randint(0,5)
    return pasir
def hitung_batu() :
    batu=0
    batu+= randint(0,5)
    return batu
def hitung_air() :
    air=0
    air+= randint(0,5)
    return air        

#PROGRAM UTAMA
def batchkumpul(users, bahan_bangunan, candi) :
    total_pasir = 0
    total_batu = 0
    total_air = 0
    if hitung_pengumpul(users)>0 :
        for i in range(hitung_pengumpul(users)) : 
            total_pasir += hitung_pasir() #hitung pasir 
            total_batu += hitung_batu() #hitung batu 
            total_air += hitung_air() #hitung pasir air
        bahan_bangunan[0][2] = int(bahan_bangunan[0][2])
        bahan_bangunan[1][2] = int(bahan_bangunan[1][2])
        bahan_bangunan[2][2] = int(bahan_bangunan[2][2])
        bahan_bangunan[0][2] += total_pasir
        bahan_bangunan[1][2] += total_batu
        bahan_bangunan[2][2] += total_air
        bahan_bangunan[0][2] = str(bahan_bangunan[0][2])
        bahan_bangunan[1][2] = str(bahan_bangunan[1][2])
        bahan_bangunan[2][2] = str(bahan_bangunan[2][2])
        
        print(f"Mengerahkan {hitung_pengumpul(users)} jin untuk mengumpulkan bahan.")
        print(f"Jin menemukan total {total_pasir} pasir, {total_batu} batu, dan {total_air} air.")
    else : 
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    return (users, bahan_bangunan, candi)