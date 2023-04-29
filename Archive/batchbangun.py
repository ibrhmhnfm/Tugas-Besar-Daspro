#FUNGSIONAL YANG DIPERLUKAN
import function
def hitung_pembangun(users) :
    pembangun=0
    for i in range(102) : 
        if users[i][2]=="pembangun" :
            pembangun+=1
    return pembangun
def hitung_pasir(candi) :
    pasir=0
    for i in range(100) :
        if candi [i][0] != None:
            pasir+= int(candi[i][2])
    return pasir
def hitung_batu(candi) :
    batu=0
    for i in range(100) :
        if candi [i][0] != None:
            batu+=int(candi[i][3])
    return batu
def hitung_air(candi) :
    air=0
    for i in range(100) :
        if candi [i][0] != None:
            air+=int(candi[i][4])
    return air        

#PROGRAM UTAMA
import random
def batchbangun(users, bahan_bangunan, candi) :
    if hitung_pembangun(users)>0 :
        for i in range(hitung_pembangun(users)) : 
            candi[i][2]=int(candi[i][2]) #hitung pasir 
            candi[i][2]+=random.randint(0,5)
            candi[i][2]=str(candi[i][2])
            candi[i][3]=int(candi[i][3]) #hitung batu 
            candi[i][3]+=random.randint(0,5)
            candi[i][3]=str(candi[i][3])
            candi[i][4]=int(candi[i][4]) #hitung pasir air
            candi[i][4]+=random.randint(0,5)
            candi[i][4]=str(candi[i][4])
        sisapasir= int(bahan_bangunan[0][2])-hitung_pasir(candi)
        sisabatu= int(bahan_bangunan[1][2])-hitung_batu(candi)
        sisaair= int(bahan_bangunan[2][2])-hitung_pasir(candi)
        
        print(f"Mengerahkan {hitung_pembangun(users)} jin untuk membangun candi dengan total bahan {hitung_pasir(candi)} pasir,{hitung_batu(candi)} batu, dan {hitung_air(candi)} air.")
        if sisapasir>=0 and sisabatu>=0 and sisaair >=0 : 
            print(f"Jin berhasil membangun total {hitung_pembangun(users)} candi.")
        else :
            print(f"Bangun gagal. Kurang {function.absolute(sisapasir)} pasir, {function.absolute(sisabatu)} batu, dan {function.absolute(sisaair)} air.")
    else : 
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    return (users, bahan_bangunan, candi)

#Test

#KOMEN #for i in range(1,4) : 

    #bahan_bangunan[i][2]=int(bahan_bangunan[i][2])
    #bahan_bangunan[i][2]+=random.randint(0,5)
    #bahan_bangunan[i][2]=str(bahan_bangunan[i][2])
#bahan_bangunan[1][2] = int(bahan_bangunan[1][2])
    #bahan_bangunan[1][2] += random.randint(0,5)
    #bahan_bangunan[1][2] = str(bahan_bangunan[1][2]