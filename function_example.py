nama_hewan = []

def tambah_nama_hewan(nama):
    nama_hewan.append(nama)
    for hewan in nama_hewan:
        print(hewan)
    print("-------")

tambah_nama_hewan("jerapah")
tambah_nama_hewan("singa")
tambah_nama_hewan("kudanil")
tambah_nama_hewan("berang-berang")

#def total(x, y):
#    total = x / y
#    return(total)

#jumlah = total(10, 5)
#print(jumlah)