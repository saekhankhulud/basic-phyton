# buku kontak
kontak = {}

daftar_kontak = []
daftar_kontak.append(kontak)

# show kontak
def lihat_kontak():
    global kontak, daftar_kontak
    if len(kontak) <= 0:
        print("Daftar Kontak:")
        print()
    else:
        print("Daftar Kontak:")
        for kontak in daftar_kontak:
            print("Nama: {}".format (kontak["nama"]))
            print("No Telepon: {}".format (kontak["no telepon"]))

# input kontak
def isi_kontak():
    kontak["nama"] = input("Nama: ")
    kontak["no telepon"] = input("No Telepon: ")
    print("Kontak berhasil ditambahkan")
    
# menu
print("Selamat datang!")

def isi_menu():
    print("--- Menu ---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")

while True:
    isi_menu()

    menu = int(input("Pilih Menu: "))

    if menu == 1:
        lihat_kontak()
    elif menu == 2:
        isi_kontak()
    elif menu == 3:
        print("Program selesai, sampai jumpa!")
        exit()
    else:
        print("Menu tidak tersedia")

