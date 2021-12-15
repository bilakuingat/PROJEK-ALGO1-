import csv
import os
import getpass

csv_filename = 'Data/Data.csv'
import time

# clearscreen ubntuk membersihkan layar dengan key cls = clearscreen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def login ():
    clear_screen()
    print("--------Silahkan Login--------")
    print("-------------Owner------------")
    User =input("Masukkan Username : ")
    Psw = getpass.getpass ("Masukkan Password : ")
    print("------------------------------")
    print("--------Terima Kasih----------")
    if User == "Admin" and Psw == "Admin":
        input("Login Sukses >>>")
        show_menu()
    else :
        login()

# Menampilkan menu program
def show_menu():

    clear_screen()
#   Baris kode untuk jumlah total data
    Barang = []
    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Barang.append(row)
    row_count = sum(1 for row in Barang)

    print("=== APLIKASI Inventory TOKO === \n")
    print("============ Menu =============")
    print("* INFO Total Barang : ",row_count)  
    print("===============================")
    print("[1] Lihat Daftar Barang")
    print("[2] Tambah Barang")
    print("[3] Edit Barang")
    print("[4] Hapus Barang")
    print("[5] Cari Barang")
    print("[0] Exit \n")
    print("===============================")
    selected_menu = input("Pilih menu> ")
    
    # Percabangan untuk menentukan pilihan menu
    if(selected_menu == "1"):
        show_barang()
    elif(selected_menu == "2"):
        tambah_barang()
    elif(selected_menu == "3"):
        edit_barang()
    elif(selected_menu == "4"):
        delete_barang()
    elif(selected_menu == "5"):
        search_barang()
    elif(selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()

# fungsi kembali ke menu isinya memanggil fungsi show menu
def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()

# fungsi menampilkan barang 
def show_barang():
    clear_screen()
    Barang = []
# buka file CSV dengan mode R / Baca
    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Barang.append(row)

    row_count = sum(1 for row in Barang)

    print("-" * 67)
    print("\t\tDaftar Stok Barang Toko")
    print("-" * 67)

    print("kode \t NAMA \t\t harga \t\t QTY  \t\t JENIS \t\t EXP")
    print("-" * 67)

    # Looping untuk mengeluarkan datanyna
    for data in Barang:
        print(f"{data['Kode']} \t {data['NAMA']} \t\t Rp.{data['HARGA']} \t {data['QTY']} \t\t {data['JENIS']} \t {data['EXP']} \t\t")
    print("-" * 67)
    print("Total Data: ",row_count)
    print("-" * 67)
    
    back_to_menu()

#  fungsi tambah barang 
def tambah_barang():
    clear_screen()
    with open(csv_filename, mode='a',newline='') as csv_file:
        fieldnames = ['kode', 'NAMA', 'harga','QTY','JENIS', 'EXP']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        print("===============================")
        print("======== Tambah Barang ========")
        print("===============================\n")
        
        kode = input("kode: ")
        nama = input("Nama Barang: ")
        harga = input("Harga Barang: ")
        QTY = input("Jumlah Barang: ")
        jenis = input("Jenis Barang: ")
        exp = input('Tanggal expired:')

        print("===============================")


        writer.writerow({'kode': kode, 'NAMA': nama, 'harga': harga, 'QTY': QTY, 'JENIS': jenis, 'EXP': exp})    
    
    back_to_menu()


def search_barang():
    clear_screen()
    Barang = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Barang.append(row)

    kode = input("Cari berdasrakan kode> ")

    data_found = []

    # mencari Barang
    indeks = 0
    for data in Barang:
        if (data['Kode'] == kode):
            data_found = Barang[indeks]
            
        indeks = indeks + 1

    if len(data_found) > 0:
        print("DATA DITEMUKAN: ")
        print(f"NAMA: {data_found['NAMA']}")
        print(f"HARGA: Rp.{data_found['HARGA']}")
        print(f"QTY :{data_found['QTY']}")
        print(f"JENIS :{data_found['JENIS']}")
        print(f"EXP :{data_found['EXP']}")
    else:
        print("Tidak ada data ditemukan")
    back_to_menu()
    
# Fungsi mengedit data barang
def edit_barang():
    clear_screen()
    Barang = []

    with open(csv_filename, mode="r",newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Barang.append(row)
    row_count = sum(1 for row in Barang)

    print("-" * 67)
    print("\t\tDaftar Stok Barang Toko")
    print("-" * 67)

    print("kode \t NAMA \t\t Harga \t\t QTY \t\t JENIS \t\t EXP")
    print("-" * 67)

    for data in Barang:
        print(f"{data['Kode']} \t {data['NAMA']} \t Rp.{data['HARGA']} \t {data['QTY']} \t {data['JENIS']} \t {data['EXP']}")

    print("-" * 67)
    print("Total Data :",row_count)
    print("-" * 67)
    kode = input("Pilih Kode Barang : ")
    nama = input("nama baru: ")
    harga = input("harga baru: ")
    QTY = input("JUMLAH baru: ")
    jenis = input("Jenis baru: ")
    exp = input("expired baru: ")

    # mencari Barang dan mengubah datanya
    # dengan data yang baru
    indeks = 0
    for data in Barang:
        if (data['Kode'] == kode):
            Barang[indeks]['NAMA'] = nama
            Barang[indeks]['HARGA'] = harga
            Barang[indeks]['QTY'] = QTY
            Barang[indeks]['JENIS'] = jenis
            Barang[indeks]['EXP'] = exp
        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['Kode', 'NAMA', 'HARGA','QTY','JENIS', 'EXP']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in Barang:
            writer.writerow({'Kode': new_data['Kode'], 'NAMA': new_data['NAMA'], 'HARGA': new_data['HARGA'], 'QTY': new_data['QTY'], 'JENIS': new_data['JENIS'], 'EXP': new_data['EXP']}) 

    back_to_menu()

# Fungsi menghapus barang
def delete_barang():
    clear_screen()
    Barang = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Barang.append(row)

    print("kode \t NAMA \t\t harga \t QTY \t JENIS \t EXP")
    print("-" * 67)

    for data in Barang:
        print(f"{data['Kode']} \t {data['NAMA']} \t {data['HARGA']} \t {data['QTY']} \t {data['JENIS']} \t {data['EXP']}")

    print("-----------------------------------")
    kode = input("Hapus Barang dengan KODE : ")

    indeks = 0
    for data in Barang:
        if (data['Kode'] == kode):
            Barang.remove(Barang[indeks])
        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['Kode', 'NAMA', 'HARGA', 'QTY', 'JENIS', 'EXP']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in Barang:
            writer.writerow({'Kode': new_data['Kode'], 'NAMA': new_data['NAMA'], 'HARGA': new_data['HARGA'], 'QTY': new_data['QTY'], 'JENIS': new_data['JENIS'], 'EXP': new_data['EXP']}) 

    print("Data sudah terhapus")
    back_to_menu()

if __name__ == "__main__":
    while True:
        login()

