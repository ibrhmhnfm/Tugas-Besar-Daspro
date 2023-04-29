#IMPORT FILE
import command
import argparse
import batchbangun
import batchkumpul
import hilang
import function
import lapor
import summon
import ubah
import laporcandi
import initialize
#INISIALISASI 
def exit_program():
  shouldSave: str = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
  while shouldSave != "Y" or shouldSave != "y" or shouldSave != "N" or shouldSave!= "n":
    shouldSave = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
  if shouldSave == "Y" or shouldSave == "y":
    pass
    # lakukan prosedur save
  else:
    return
parser = argparse.ArgumentParser()
parser.add_argument("folder_name", help="Nama folder yang berisi file penyimpanan")
args = parser.parse_args()


#PROSES
if __name__ == '__main__':
  if args.folder_name:
    print("Loading...")
    data = command.load_data(args.folder_name)
  else:
    print("Tidak ada nama folder yang diberikan!\n\nUsage: python main.py <nama_folder>")

# print(data)
users = command.format(data[2]) # Ubah sesuai urutan file di folder. (cek dulu sebelum dijalankan)
bahan_bangunan = command.format(data[0])
candi = command.format(data[1])
username = [None for i in range (102)]
users = function.KonsDot(users, 2, [])
candi = function.KonsDot(candi, 0, [])
users = initialize.initialize_final(initialize.initialize(users, 102, 3), 103)
candi = initialize.initialize_final(initialize.initialize(candi, 100, 5), 101)
# x = ["Admin","gacha4lyfe","admin" ] # buat ngetes (testing)
# users = function.Konso(x, users, 102)
username = initialize.initialize_username(username, users)

#MAIN PROGRAM/ALGORITHM
akses = None
is_login = False
loop = True
while loop:
    masukan = input(">>> ")
    if (masukan == "login"):
        if (is_login == False):
          (akses, is_login) = command.login(users)
        elif (is_login == True):
           print(f"Login gagal! \nAnda telah login dengan username {akses}, silahkan lakukan “logout” sebelum melakukan login kembali.")
    elif (akses == "admin"):
      if (masukan == "cekarray"):
        print("array username :",username)
      elif (masukan == "users"):
        print(users)
      elif (masukan =="candi"):
        print(candi)
      elif (masukan == "bahan_bangunan"):
        print(bahan_bangunan)
      elif (masukan =="logout"):
        is_login = False
        akses = None
        print("Berhasil logout")
    elif (masukan =="summonjin"):
      if (akses == "bandung_bondowoso"):
        (users, username) = summon.summon_jin(users, username)
      else:
        print("Summon jin hanya bisa diakses oleh akun Bandung Bondowoso")
    elif (masukan =="ubahjin"):
      if (akses == "bandung_bondowoso"):
        users = ubah.ubahjin(users, username)
      else:
        print("Ubah jin hanya bisa diakses oleh akun Bandung Bondowoso")
    elif (masukan =="hapusjin"):
      if (akses == "bandung_bondowoso"):
        (users, candi, username)= hilang.hilang(users, candi, username)
      else:
        print("Hapus jin hanya bisa diakses oleh akun Bandung Bondowoso")
    elif (masukan =="batchbangun"):
      if (akses == "bandung_bondowoso"):
        print(bahan_bangunan)
        (users, bahan_bangunan, candi) = batchbangun.batchbangun(users, bahan_bangunan, candi)
        print(bahan_bangunan)
      else:
        print("Batch bangun hanya bisa diakses oleh akun Bandung Bondowoso")
    elif (masukan =="batchkumpul"):
      if (akses == "bandung_bondowoso"):
        (users, bahan_bangunan, candi) = batchkumpul.batchkumpul(users, bahan_bangunan, candi)
      else:
        print("Batch kumpul hanya bisa diakses oleh akun Bandung Bondowoso")
    elif (masukan =="laporanjin"):
      if (akses == "bandung_bondowoso"):
        lapor.laporjin(users, username, bahan_bangunan, candi)
      else:
        print("Laporan jin hanya bisa diakses oleh akun Bandung Bondowoso")
    elif (masukan =="laporancandi"):
      if  (akses == "bandung_bondowoso"):
        laporcandi.laporan_candi(candi)
      else:
        print("Laporan candi hanya bisa diakses oleh akun Bandung Bondowoso")
    elif (masukan =="hancurkancandi"):
      if (akses =="roro_jonggrang"):
        print("belum dibuat, harap tunggu")
      else:
        print("Hancurkan candi hanya bisa diakses oleh akun Roro Jonggrang")
    elif (masukan =="ayamberkokok"):
      if (akses =="roro_jonggrang"):
        print("belum dibuat, harap tunggu")
      else:
        print("Ayam berkokok hanya bisa diakses oleh akun Roro Jonggrang")
    elif (masukan == "kumpul"):
      if (akses =="pengumpul"):
        print("ngumpul")
      else :
        print("Kumpul hanya bisa diakses oleh akun jin pengumpul")
    elif (masukan == "bangun"):
      if (akses =="pembangun"):
        print("ngebangun")
      else :
        print("Bangun hanya bisa diakses oleh akun jin pembangun")
    elif (masukan == "logout"):
       (akses, is_login) = command.logout(akses, is_login)
    elif masukan == "help":
       command.show_help(akses)
    elif (masukan == "exit"):
       exit_program()
       loop = False