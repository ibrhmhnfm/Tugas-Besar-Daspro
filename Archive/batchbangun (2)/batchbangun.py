#VARIABEL GLOBAL
tampung_jin=[[0 for i in range(3)] for j in range(102)]
tampung_jin[0][0] = "jin1"
tampung_jin[0][1] = "12345"
tampung_jin[0][2] = "pembangun"
tampung_jin[2][0] = "jin2"
tampung_jin[2][1] = "12345"
tampung_jin[2][2] = "pembangun"
#[[Username,Password,role]]
bahan_bangunan=[['nama','deskripsi','jumlah'],['pasir','-','10'],['batu','-','10'],['air','-','10']]
#[[nama,deskripsi,jumlah]]
candi=[[0 for i in range(5)] for j in range(100)]
#[[id,Pembuat,pasir,batu,air]]

#FUNGSIONAL YANG DIPERLUKAN
def hitung_pembangun () :
    global tampung_jin
    pembangun=0
    for i in range(100) : 
        if tampung_jin[i][2]=="pembangun" :
            pembangun+=1
    return pembangun
def hitung_pasir() :
    global candi 
    pasir=0
    for i in range(100) :
        pasir+= int(candi[i][2])
    return pasir
def hitung_batu() :
    global candi 
    batu=0
    for i in range(100) :
        batu+=int(candi[i][3])
    return batu
def hitung_air() :
    global candi 
    air=0
    for i in range(100) :
        air+=int(candi[i][4])
    return air        
def nama_bangun () : 
    global tampung_jin
    nama=[]
    for i in range(102) : 
        if tampung_jin[i][2]=="pembangun" :
            nama.append(tampung_jin[i][0])
    return nama

#PROGRAM UTAMA
import random
def batchbangun() :
    global bahan_bangunan
    global candi
    if hitung_pembangun()>0 :
        for i in range(hitung_pembangun()) : 
            candi[i][2]=int(candi[i][2]) #hitung pasir 
            candi[i][2]+=random.randint(1,5)
            candi[i][2]=str(candi[i][2])
            candi[i][3]=int(candi[i][3]) #hitung batu 
            candi[i][3]+=random.randint(1,5)
            candi[i][3]=str(candi[i][3])
            candi[i][4]=int(candi[i][4]) #hitung pasir air
            candi[i][4]+=random.randint(1,5)
            candi[i][4]=str(candi[i][4])

        sisapasir= int(bahan_bangunan[1][2])-hitung_pasir()
        sisabatu= int(bahan_bangunan[2][2])-hitung_batu()
        sisaair= int(bahan_bangunan[3][2])-hitung_air()
        if sisapasir>0 or sisaair>0 or sisabatu>0 :
            bahan_bangunan[1][2]=sisapasir
            bahan_bangunan[2][2]=sisabatu
            bahan_bangunan[3][2]=sisaair
        nama_pembangun=nama_bangun()
        for j in range(hitung_pembangun()) :
            candi[j][1]= nama_pembangun[j]
        
        print(f"Mengerahkan {hitung_pembangun()} jin untuk membangun candi dengan total bahan {hitung_pasir()} pasir,{hitung_batu()} batu, dan {hitung_air()} air.")
        if sisapasir>=0 and sisabatu>=0 and sisaair >=0 : 
            print(f"Jin berhasil membangun total {hitung_pembangun()} candi.")
        else :
            print(f"Bangun gagal. Kurang {sisapasir} pasir, {sisabatu} batu, dan {sisaair} air.")
    else : 
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
#Test
batchbangun()
print(candi)
print(tampung_jin)
