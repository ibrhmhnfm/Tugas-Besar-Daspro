import function
def summon_jin(users, username) : 
    global tampung_jin
    tampung_jin = users
    summoned = False
    print("Jenis jin yang dapat dipanggil:")
    print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
    print("(2) Pembangun - Bertugas membangun candi ")
    ID=input("Masukkan nomor jenis jin yang ingin dipanggil:")
    jin=""
    if hitung_pembangun()+hitung_pengumpul()==100 :
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    else : 
        if int(ID)==1 : 
            print(f"\nMemilih jin pengumpul")
            cek = True
            while cek :   
                user=str(input("\nMasukkan username jin: "))
                i=0
                status=True
                while status:
                    if function.inlist(user,username,102)==True : 
                        print(f"\nUsername {user} sudah diambil!")
                        status = False
                    else : 
                        password = input("Masukkan password jin: " )
                        while not(5<=len(password)<=25) :
                            print("\nPassword panjangnya harus 5-25 karakter!")
                            password = input("\nMasukkan password jin: " )
                        summoned = True
                        cek = False
                        status=False
            jin="pengumpul"
        elif int(ID)==2 : 
            print(f"\nMemilih jin pembangun")
            cek = True
            while cek :   
                user=str(input("\nMasukkan username jin: "))
                i=0
                status=True
                while status:
                    if function.inlist(user,username,102)==True : 
                        print(f"\nUsername {user} sudah diambil!")
                        status = False
                    else : 
                        password = input("Masukkan password jin: " )
                        while not(5<=len(password)<=25) :
                            print("\nPassword panjangnya harus 5-25 karakter!")
                            password = input("\nMasukkan password jin: " )
                        summoned = True
                        status=False
                        cek = False
            jin="pembangun"
        else :
            print(f"Tidak ada jenis jin bernomor “{ID}”")
    if summoned:
        j = 0
        while j < 102 : 
            if tampung_jin[j][1] == None:
                tampung_jin[j][0]=user
                tampung_jin[j][1]=password
                tampung_jin[j][2]=jin
                username[j] = user
                j = 102
            else:
                j += 1
        print("\nMengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...")
        print(f"\nJin {user} berhasil dipanggil!")
    return (tampung_jin, username)
def hitung_pengumpul () :
    global tampung_jin
    pengumpul=0
    for i in range(102) : 
        if tampung_jin[i][2]=="pengumpul" :
            pengumpul+=1
    return pengumpul

def hitung_pembangun () :
    global tampung_jin
    pembangun=0
    for i in range(102) : 
        if tampung_jin[i][2]=="pembangun" :
            pembangun+=1
    return pembangun

