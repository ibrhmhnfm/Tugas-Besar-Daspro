#VARIABEL GLOBAL
tampung_jin=[[0 for i in range(3)] for j in range(102)]
tampung_jin[0][0] = "jin1"
tampung_jin[0][1] = "12345"
tampung_jin[0][2] = "pembangun"
tampung_jin[2][0] = "jin2"
tampung_jin[2][1] = "12345"
tampung_jin[2][2] = "pembangun"
tampung_jin[3][0] = "jin3"
tampung_jin[3][1] = "12345"
tampung_jin[3][2] = "pembangun"
#[[Username,Password,role]]
bahan_bangunan=[['nama','deskripsi','jumlah'],['pasir','-','10'],['batu','-','10'],['air','-','10']]
#[[nama,deskripsi,jumlah]]
candi=[[0 for i in range(5)] for j in range(100)]
#[[id,Pembuat,pasir,batu,air]]

import random
def totalefektif(a) :
    count = 0
    i = 0
    while True:
        if a[i][1] != "":
            count += 1
            i += 1
        else:
            break
    return count

#REALISASI PROSEDUR
def batchbangun() :
    global bahan_bangunan
    global candi
    totalpasir=totaljin=totalbatu=totalair=totalterbangun=0
    pembangun=["" for i in range(100)]
    kapasitascandi=150-totalefektif(candi)-1

    for i in range(102) : 
        if tampung_jin[i][2]=="pembangun" and kapasitascandi!=0 :
            totaljin+=1
            pasir=random.randint(1,5)
            batu=random.randint(1,5)
            air=random.randint(1,5)
            totalpasir+=pasir
            totalair+=air
            totalbatu+=batu
            pembangun[totaljin-1]=tampung_jin[i][0]
            kapasitascandi-=1
    print(f"Mengerahkan {totaljin} jin untuk membangun candi dengan total bahan {totalpasir} pasir,{totalbatu} batu, dan {totalair} air.")
    if (totalpasir > bahan_bangunan[1][2]) or (totalbatu > bahan_bangunan[2][2]) or (totalair > bahan_bangunan[3][2]):
        kurangpasir = totalpasir - bahan_bangunan[1][2]
        kurangbatu = totalbatu - bahan_bangunan[2][2]
        kurangair = totalair - bahan_bangunan[3][2]

        if kurangpasir < 0:
            kurangpasir = 0
        if kurangbatu < 0:
            kurangbatu = 0
        if kurangair < 0:
            kurangair = 0
        print(f"Bangun gagal. Kurang {kurangpasir} pasir, {kurangbatu} batu, dan {kurangair} air.")
    else:
        i = 1
        for j in range(totaljin):
            while i <= 150:
                if candi[i][1] == "":#
                    candi[i][0] = i
                    candi[i][1] = pembangun[j]
                    candi[i][2] = pasir
                    candi[i][3] = batu
                    candi[i][4] = air
                    bahan_bangunan[1][2] -= pasir
                    bahan_bangunan[2][2] -= batu 
                    bahan_bangunan[3][2] -= air
                    #jika bahan bangunan overlap mengurangi kurang dari nol
                    for j in range(3):
                        if bahan_bangunan[j+1][2] < 0:
                            bahan_bangunan[j+1][2] = 0
                    totalterbangun += 1
                    break
                else:
                    i += 1
        print(f"Jin berhasil membangun total {totalterbangun} candi.")
batchbangun()
print(bahan_bangunan)
print(candi)