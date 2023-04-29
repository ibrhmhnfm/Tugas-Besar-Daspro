from random import randint
import function

# fungsional tambahan
def hitungpembangun (users):
    count = 0
    for i in range (102):
        if users[i][2] == "pembangun":
            count += 1
    return count

def username_pembangun (users):
    arrnew = []
    j = 0
    for i in range (102):
        if users[i][2] == "pembangun":
            arrnew = function.KonsDot(arrnew, j, users[i][0])
            j += 1
    return arrnew

# randomizer_kebutuhan
def randomizer_kebutuhan ():
    butuh_pasir = randint(1,5)
    butuh_batu = randint(1,5)
    butuh_air = randint(1,5)
    return (butuh_pasir, butuh_batu, butuh_air)

# pengecek ada-kurangnya bahan
def bahan_cukup (bahan_bangunan, total_butuh_pasir, total_butuh_batu, total_butuh_air):
    cukup = False
    sisa_pasir = int(bahan_bangunan[0][2]) - total_butuh_pasir
    sisa_batu = int(bahan_bangunan[1][2]) - total_butuh_batu
    sisa_air = int(bahan_bangunan[2][2]) - total_butuh_air
    if sisa_pasir >= 0 and sisa_batu >= 0 and sisa_air >= 0:
        cukup = True
    return (cukup, sisa_pasir, sisa_batu, sisa_air)
# mengassign candi baru
def index_isi_candi (candi):
    idx = 0
    while candi[idx] != [None, None, None, None, None]:
        idx += 1
    return idx

# Program utama
def batchbangun (users, bahan_bangunan, candi):
    r = hitungpembangun(users)
    candi_bangun = 0
    if  r > 0:
        butuh_pasir = []
        butuh_batu = []
        butuh_air = []
        for i in range (r):
            butuh_pasir = function.KonsDot(butuh_pasir, i, randomizer_kebutuhan()[0])
            butuh_batu = function.KonsDot(butuh_batu, i, randomizer_kebutuhan()[1])
            butuh_air = function.KonsDot(butuh_air, i, randomizer_kebutuhan()[2])
        total_butuh_pasir = function.sumarr(butuh_pasir, r)
        total_butuh_batu = function.sumarr(butuh_batu, r)
        total_butuh_air = function.sumarr(butuh_air, r)
        print(f"Mengerahkan {r} jin untuk membangun candi dengan total bahan {total_butuh_pasir} pasir, {total_butuh_batu} batu, dan {total_butuh_air} air.")
        sisa_pasir = bahan_cukup(bahan_bangunan, total_butuh_pasir, total_butuh_batu, total_butuh_air )[1]
        sisa_batu = bahan_cukup(bahan_bangunan, total_butuh_pasir, total_butuh_batu, total_butuh_air )[2]
        sisa_air = bahan_cukup(bahan_bangunan, total_butuh_pasir, total_butuh_batu, total_butuh_air )[3]
        if bahan_cukup(bahan_bangunan, total_butuh_pasir, total_butuh_batu, total_butuh_air )[0]:
            candi_bangun = r
            print(f"Jin berhasil membangun total {candi_bangun} candi.")
            bahan_bangunan[0][2]=sisa_pasir
            bahan_bangunan[1][2]=sisa_batu
            bahan_bangunan[2][2]=sisa_air
            sisa = candi_bangun
            i = 0
            while sisa != 0:
                idx = index_isi_candi(candi)
                candi[idx][0]= idx+1
                candi[idx][1]= username_pembangun(users)[i]
                print(butuh_pasir)
                print(butuh_batu)
                print(butuh_air)
                print(username_pembangun(users))
                candi[idx][2]= butuh_pasir[i]
                candi[idx][3]= butuh_batu[i]
                candi[idx][4]= butuh_air[i]
                i += 1
                sisa -= 1
        else:
            print(f"Bangun gagal. Kurang {function.absolute(sisa_pasir)} pasir, {function.absolute(sisa_batu)} batu, dan {function.absolute(sisa_air)} air.")
    else : 
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    return (users, bahan_bangunan, candi)