# #dengan method procedure
phi = 3.14
r = float(input("masukkan jari-jari lingkaran : "))

def luas_lingkaran (luas):
    luas = phi*r*r
    print("Luas lingkaran adalah : ", str(luas))

def keliling (keliling):
    keliling = 2*phi*r
    print("keliling lingkaran adalah : ", str(keliling))

luas_lingkaran(r)
keliling(keliling)

#dengan method function

def luas_lingkaran(r):
    luas = phi * r * r
    return luas

def keliling_lingkaran(r):
    keliling = 2 * phi * r
    return keliling

phi =3.14
r = float(input("Masukkan jari-jari lingkaran: "))

luas = luas_lingkaran(r)
keliling = keliling_lingkaran(r)

print("Luas lingkaran adalah:", luas)
print("Keliling lingkaran adalah:", keliling)



