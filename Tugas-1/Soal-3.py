nilai_teori = float(input("Masukkan nilai teori anda: "))
nilai_praktek = float(input("Masukkan nilai praktek anda: "))
nilai_min = 70

if nilai_teori >= nilai_min and nilai_praktek >= nilai_min:
    print("Selamat, anda lulus!")
elif nilai_teori >= nilai_min and nilai_praktek < nilai_min:
    print("Anda harus mengulang ujian praktek.")
elif nilai_teori < nilai_min and nilai_praktek >= nilai_min:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")