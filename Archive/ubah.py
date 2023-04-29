import function
def ubahjin(users, username) : 
    user=input("Username jin yang ingin diubah :") 
    idx=0
    if  function.inlist(user,username,102): 
        idx = function.get_index(user, username, 102)
        if users[idx][2]=="pengumpul" :
            yakin=input('Jin ini bertipe “Pengumpul", Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ')
            if yakin=="Y" or yakin =="y":
                users[idx][2]="pembangun"
                print("Jin telah berhasil diubah") 
        elif users[idx][2]=="pembangun" : 
            yakin=input('Jin ini bertipe “Pembangun", Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ')
            if yakin=="Y" or yakin =="y" :
                users[idx][2]="pengumpul"
                print("jin telah berhasil diubah")
    else : 
        print("Tidak ada jin dengan username tersebut.")
    return users

