""" ================= Fungsi Custom ================= """

def createarr(a):  # Buat bikin gampang inisialisasi array
    arr = [0 for i in range(a)]
    return arr
# x : yg mau dimasukin, arr : array tujuan x, r : panjang array (harusny statis, jadi diketahui.)

def Konso(x, arr, r):  # Menambah x ke array, x di depan. Return berupa array (ganti .append())
    arrnew = createarr(r+1)
    for i in range(1, r):
        arrnew[i] = arr[i-1]
    arrnew[0] = x
    return arrnew
# x : yg mau dimasukin, arr : list tujuan x, r : panjang list


def KonsDot(arr, r, x):  # Menambah x ke list, x di belakang. Return berupa list (ganti .append())
    arrnew = createarr(r+1)
    for i in range(0, r):
        arrnew[i] = arr[i]
    arrnew[r] = x
    return arrnew
# list : list yang mau ditambahin elemennya, r : panjang list


def sumarr(arr, r):  # Jumlah semua dalam list (ganti .sum())
    suml = 0
    for i in range(r):
        suml += arr[i]
    return suml
# x : elemen yg mau dicari ada atau engg nya, list: list yang dicek, r : panjang list


def inlist(x, arr, r):  # Menentuin ada elemen di list atau engg. True kl ada, False kl engg. (ganti 'in')
    inside = False
    for i in range(r):
        if x == arr[i]:
            inside = True
    return inside


def delso(arr, r):  # fungsi buat ngehapus elemen pertama (memperpendek list)
    arrnew = createarr(r-1)
    for i in range(r-1):
        arrnew[i] = arr[i+1]
    return arrnew


def delsdot(arr, r):  # fungsi buat menghapus elemen terakhir (memperpendek list)
    arrnew = createarr(r-1)
    for i in range(r-1):
        arrnew[i] = arr[i]
    return arrnew


def delfl1(x, arr, r):  # fungsi buat delfromlist, menukar nilai x yg pertama kali ditemukan ke belakang list
    for i in range(r):
        if x == arr[i]:
            for j in range(i, r):
                if j+1 in range(r):
                    temp = arr[j+1]
                    arr[j] = temp
                else:
                    break
    return delsdot(arr, r)


def delfromarr(x, arr, r):  # fungsi buat menghapus semua nilai x di list (ganti .pop())
    while inlist(x, arr, r):
        arr = delfl1(x, arr, r)
        r -= 1
    return arr


def slicefront(arr, i):  # gantiin arr[:i]
    arrnew = createarr(i)
    for j in range(i):
        arrnew[j] = arr[j]
    return arrnew


def sliceback(arr, a, r):  # gantiin arr[i:]
    arrnew = createarr(r-a)
    for i in range(a, r):
        j = i - a
        arrnew[j] = arr[i]
    return arrnew


def sort(arr, r):  # pengganti sorted()
    switch = False
    for i in range(r-1):
        for j in range(0, r-i-1):
            if arr[j] > arr[j+1]:
                switch = True
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        if not switch:
            break
    return arr


def get_index(x, arr, r):  # ganti .index()
    index = ""
    for i in range(r):
        if x == arr[i]:
            index = i
            break
    return index

def joinwords(arrstr):  # fungsi buat nambahin array of char jadi kata
    word = ''
    for i in range(len(arrstr)):  # len boleh utk string
        word += arrstr[i]
    return word

def split(li, banyak, str):  # ganti .split()
    r = len(li)  # len boleh u/ string
    listnew = createarr(banyak)
    for i in range(banyak):
        a = get_index(str, li, r)
        if inlist(str, li, r):
            if a == 0:
                li = delso(li, r)
                r -= 1
                a = get_index(str, li, r)
            listnew1 = slicefront(li, a)
            li = sliceback(li, a, r)
            li = delso(li, (r-a))
            r -= (a+1)
            listnew[i] = joinwords(listnew1)
            if r > 0 and not inlist(str, li, r):
                listnew[i+1] = joinwords(li)
        else:
            break
    return listnew


def max_array(arr, r):
    max = 0
    for i in range(r):
        if arr[i] > max:
            max = arr[i]
    return max


def min_array(arr, r):
    min = 100000000
    for i in range(r):
        if arr[i] < min:
            min = arr[i]
    return min

# mengembalikan array baru dengan elemen pada index yang ditentukan telah dihapus
# (pengganti keyword del)


def del_by_index(li, index, length):
    # li adalah list yang elemennya mau dihapus
    # index adalah index posisi elemen yang mau dihapus
    # length adalah panjang list yang elemennya mau dihapus
    arr = createarr(length-1)
    indeksarr = 0
    for i in range(length):
        if i != index:
            arr[indeksarr] = li[i]
            indeksarr += 1
    return arr

def arr_length(array): # Panjang array, pengganti len()
    count = 0
    for i in array:
        count += 1
    return count

def find_index_arr(arr, item):
    for i in range(arr_length(arr)):
        if arr[i] == item:
            return i
    return ""

def find_index_row(matrix, item): # Mencari index baris pada matriks
    for i in range(arr_length(matrix)):
        for j in range(arr_length(matrix[i])):
            if matrix[i][j] == item:
                return i
    return ""

def join(arr):
    result = ""
    for i in arr:
        result += i
    return result

def concatenate_strings(strings, delimiter=''):
    result = ''
    for i in range(len(strings)):
        result += strings[i]
        if i != len(strings) - 1:
            result += delimiter
    return result

def my_append(list, item): # Pengganti .append()
    list += [item]
    return list

def my_split(string, separator): # Pengganti .split()
    result = []
    current_part = ''
    
    for char in string:
        if char != separator:
            current_part += char
        else:
            my_append(result, current_part)
            current_part = ''
    
    if current_part:
        my_append(result, current_part)
    
    return result

def arr_slice(arr, start_idx): # Pengganti arr[i:]
    sliced_arr = []
    for i in range(start_idx, arr_length(arr)):
        my_append(sliced_arr, arr[i])
    return sliced_arr

# def format(data): # Mengubah csv menjadi array of array [[baris1], [baris2], [baris3], dst....]
#     rows = data.split('\n')

#     # membagi baris menjadi kolom dan memasukkan ke dalam list
#     new_data = []
#     for row in rows:
#         cols = row.split(',')
#         new_data.append(cols)
#     return new_data

def format(data): # Mengubah csv menjadi array of array [[baris1], [baris2], [baris3], dst....]
    # Membagi string menjadi beberapa baris
    rows = my_split(data, '\n')
    # Membagi setiap baris menjadi beberapa kolom
    new_data_wheader = [my_split(row, ';') for row in rows if row]
    # Hapus header
    new_data = new_data_wheader[1:]
    return new_data

def id(data):
    header = data[0].strip().split(';')
    id_index = header.index('id')
    ids = []
    for line in data:
        values = line.strip().split(';')
        ids.append(int(values[id_index]))
    return ids

def csv_join(strings, separator=','):
    result = ""
    for i, s in my_enumerate(strings):
        if i > 0:
            result += separator
        result += s
    return result

def my_enumerate(iterable, start=0):
    result = []
    for i in range(arr_length(iterable)):
        my_append(result, (i + start, iterable[i]))
    return result


import os
""" ================= Fungsi Utama ================= """
def login(users):
    while True:
        # Meminta pengguna untuk memasukkan username dan password
        input_username = input("Username: ")
        input_password = input("Password: ")

        # Memeriksa apakah username dan password yang dimasukkan benar
        user_index = find_index_row(users, input_username)
        if user_index != "" and users[user_index][1] == input_password:
            akses = users[user_index][2]
            is_login = True
            print("Selamat datang,", akses)
            print("Masukkan command 'help' untuk daftar command yang dapat kamu panggil.")
            print("Anda telah login dengan username", input_username + ",", "silahkan lakukan 'logout' sebelum melakukan login kembali.")
            return akses, is_login # Return sebaiknya di akhir
        elif user_index != "" and users[user_index][1] != input_password:
            print("Password salah!")
        else:
            print("Username tidak terdaftar!")
        
def logout(akses, is_login):
    if (is_login == True) and (akses != None):
        akses = None
        is_login = False
        print("Berhasil logout")
        return akses, is_login
    # dijadiin global ()
    else:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        return None, False

def show_help(akses):
    # Output Header Help
    header_help = "="*20 + " Help " + "="*20

    # Common Command Help
    login_help = "Login \nUntuk menggunakan akun\n"
    save_help = "Save help \nMenjalankan prosedur menyimpan data yang berada di program sesuai dengan struktur data eksternal\n"
    exit_help = "Exit \nUntuk keluar dari program dan kembali ke terminal\n"
    logout_help = "Logout \nUntuk keluar dari akun yang digunakan sekarang\n"
    
    # Bandung Bondowoso Command Help
    summon_jin_help = "Summon Jin \nUntuk memanggil jin\n"
    hilangkan_jin_help = "Hilangkan Jin \nUntuk menghilangkan jin\n"
    ubah_tipe_jin_help = "Ubah tipe Jin \nUntuk mengubah tipe Jin\n"
    batch_kumpul_help = "Batch kumpul \nMengerahkan pasukan jin pengumpul untuk mengumpulkan bahan\n"
    batch_bangun_help = "Batch Bangun \nMengerahkan pasukan jin pembangun untuk membangun candi\n"
    ambil_laporan_jin_help = "Mengambil laporan jin \nMengambil laporan jin untuk mengetahui kinerja dari para jin\n"
    ambil_laporan_candi_help = "Ambil laporan candi \nMengambil laporan candi untuk mengetahui progress pembangunan candi\n"

    # Roro Jonggrang Command Help
    hancurkan_candi_help = "Hancurkan candi \nMenghancurkan candi\n"
    ayam_berkokok_help = "Ayam berkoko \nUntuk menyelesaikan permainan dengan memalsukan pagi hari\n"

    # Jin pembangun Command help
    bangun_help = "Membangun candi dari bahan yang telah dikumpulkan"

    # Jin pengumpul Command help
    kumpul_help = "Mengumpulkan bahan untuk membangun candi: pasir, batu, dan air"


    # Output Help berdasarkan akses
    if (akses == None):
        # Header
        print(header_help)
        # Command dan deskripsi
        print(f"1. {login_help}")
        print(f"2. {exit_help}")
    elif (akses == "bandung_bondowoso"):
        # Header
        print(header_help)
        # Command dan deskripsi
        print(f"1. {logout_help}")
        print(f"2. {summon_jin_help}")
        print(f"3. {hilangkan_jin_help}")
        print(f"4. {ubah_tipe_jin_help}")
        print(f"5. {batch_kumpul_help}")
        print(f"6. {batch_bangun_help}")
        print(f"7. {ambil_laporan_jin_help}")
        print(f"8. {ambil_laporan_candi_help}")
        print(f"9. {save_help}")
    elif (akses == "roro_jonggrang"):
        # Header
        print(header_help)
        # Command dan deskripsi
        print(f"1. {logout_help}")
        print(f"2. {hancurkan_candi_help}")
        print(f"3. {ayam_berkokok_help}")
        print(f"4. {save_help}")
    elif (akses == "jin_pengumpul"):
        # Header
        print(header_help)
        # Command dan deskripsi
        print(f"1. {kumpul_help}")
        print(f"2. {logout_help}")
    elif (akses == "jin_pembangun"):
        # Header
        print(header_help)
        #Command dan deskripsi
        print(f"1. {bangun_help}")
        print(f"2. {logout_help}")

def load_data(folder_name):
    list_data = []
    for filename in os.listdir(folder_name):
        if filename.endswith('.csv'):
            with open(os.path.join(folder_name, filename), 'r') as file:
                file_data = file.read()
                print(f"Data dibaca dari {os.path.join(folder_name, filename)}")
                data = my_append(list_data, file_data)
    return data

def save_data_to_csv(data, folder, mark):
    if mark == 'user':
        file_path = f"./save/{folder}/user.csv"
        headers = ['username', 'password', 'role']
    elif mark == 'candi':
        file_path = f"./save/{folder}/candi.csv"
        headers = ['id', 'pembuat', 'pasir', 'batu', 'air']
    elif mark == 'bahan_bangunan':
        file_path = f"./save/{folder}/bahan_bangunan.csv"
        headers = ['nama', 'deskripsi', 'jumlah']
        
    if not os.path.exists(file_path):
        # Jika file belum ada, buat file baru
        with open(file_path, mode='w') as file:
            file.write(csv_join(headers) + '\n')
    else:
        # Jika file sudah ada, overwrite file yang lama dengan yang baru
        with open(file_path, mode='w') as file:
            file.write(csv_join(headers) + '\n')
    with open(file_path, mode='a') as file:
        line = csv_join(data) # Ganti dengan data yang sesuai
        file.write(line + '\n')