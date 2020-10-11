r = float(input("Masukkan jari-jari lingkaran (cm): "))
Pi = 22 / 7

def hitung_luas_lingkaran(r):
    luas = Pi * r ** 2
    return luas

luas = hitung_luas_lingkaran(r)

print("Luas lingkaran dengan jari-jari {} cm adalah {:.2f} cm\u00b2".format (r, luas))