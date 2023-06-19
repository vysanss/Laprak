#dengan method function
sisi = int(input("masukkan panjang sisi : "))

def hitung_keliling_persegi(sisi):
    hasil = 4*sisi
    return hasil

def hitung_luas_persegi(sisi):
    hasil = sisi*sisi
    return hasil

print("keliling persegi : %d" % hitung_keliling_persegi(sisi))
print("luas persegi : %d" % hitung_luas_persegi(sisi))

#dengan method prosedur
panjang = int(input("masukkan panjang sisi: "))

def keliling_dan_luas_persegi(sisi):
    keliling = 4*sisi
    luas = sisi*sisi
    print("keliling persegi : %d" % keliling)
    print("luas persegi : %d" % luas)

keliling_dan_luas_persegi(panjang)


#perbandingan
bil1 = int(input("masukkan bilangan ke-1 : "))
bil2 = int(input("masukkan bilangan ke-2 : "))

def cari_bilangan_terbesar(a, b):
    if a>b :
        terbesar = a
        print("bilangan terbesar adalah {}" .format(terbesar))
    elif a<b :
        terbesar = b
        print("bilangan terbesar adalah {}" .format(terbesar))
    else :
        print("nilai bilangan sama")
        
cari_bilangan_terbesar(bil1, bil2)