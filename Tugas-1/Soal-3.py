nilai_teori = input("Masukkan nilai teori anda: ")
nilai_praktek = input("Masukkan nilai praktek anda: ")
nilai_min = 70

if float(nilai_teori) >= int(nilai_min) and float(nilai_praktek) >= int(nilai_min):
    print("Selamat, anda lulus!")
elif float(nilai_teori) >= int(nilai_min) and float(nilai_praktek) < int(nilai_min):
    print("Anda harus mengulang ujian praktek.")
elif float(nilai_teori) < int(nilai_min) and float(nilai_praktek) >= int(nilai_min):
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")