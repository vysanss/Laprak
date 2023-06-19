jumlah_kata = int(input("Masukkan jumlah kata: "))

kata = []

for i in range(jumlah_kata):
    kata2 = input("Masukkan kata : ")
    kata.append(kata2)

cari_kata = input("Masukkan Kata yang ingin Anda cari: ")

if cari_kata in kata:
    print("Kata ditemukan!")
else:
    print("Kata tidak ditemukan!")

