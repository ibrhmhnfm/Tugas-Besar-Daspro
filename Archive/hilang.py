import function

def hilang(users, candi, username) : 
    idx=0 
    user=input("Masukkan username jin : ") 
    status = True
    while status: 
        if function.inlist(user, username, 102):
            yakin=input(f"Apakah anda yakin ingin menghapus jin dengan username {user} (Y/N)? ")
            if yakin=="Y" or yakin =="y":
                print("Jin telah berhasil dihapus dari alam gaib")
                users[function.get_index(user, username, 102)] = [None, None, None]
                username[function.get_index(user, username, 102)] = None
                for i in range(100) :
                    if str(candi[i][1]) == user   :       
                        for j in range(5) :
                            candi[i][j]= None
                status = False
            elif yakin =="N" or yakin =="n":
                print("Jin tidak jadi dihapus")
                status = False
        else : 
            print("Tidak ada jin dengan username tersebut.")
            status = False
    return (users, candi, username)
