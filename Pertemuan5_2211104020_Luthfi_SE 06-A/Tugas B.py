jumlah_nilai = int(input("Masukkan jumlah nilai: "))

total_nilai = 0

for i in range(jumlah_nilai):
    nilai = float(input("Masukkan nilai ke-{}: ".format(i+1)))
    total_nilai += nilai

rata_rata = total_nilai / jumlah_nilai

if 100 > rata_rata >= 90:
    predikat = "A"
elif 90 > rata_rata >= 70:
    predikat = "B"
elif 70 > rata_rata >= 50:
    predikat = "C"
elif 50 > rata_rata >= 30:
    predikat = "D"
elif 30 > rata_rata >= 0:
    predikat = "E"
else:
    predikat = "Tidak Valid"

print("Rata-rata:", (rata_rata))
print("Predikat: ", predikat)
