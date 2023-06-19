# #dengan method function
# def tambah(i, j):
#     return i + j

# def kurang(i, j):
#     return i - j

# def kali(i, j):
#     return i * j

# def bagi(i, j):
#     return i / j

# def pangkat(i, j):
#     return i ** j

# while True:
#     print("             KALKULATOR")
#     print("1. Penjumlahan")
#     print("2. Pengurangan")
#     print("3. Perkalian")
#     print("4. Pembagian")
#     print("5. Pangkat")

#     pilihan = input("Masukkan pilihan : ")

#     if pilihan == "1":
#         i = float(input("Masukkan angka pertama: "))
#         j = float(input("Masukkan angka kedua: "))
#         hasil = tambah(i, j)
#         print("Hasil: ", hasil)

#     elif pilihan == "2":
#         i = float(input("Masukkan angka pertama: "))
#         j = float(input("Masukkan angka kedua: "))
#         hasil = kurang(i, j)
#         print("Hasil: ", hasil)

#     elif pilihan == "3":
#         i = float(input("Masukkan angka pertama: "))
#         j = float(input("Masukkan angka kedua: "))
#         hasil = kali(i, j)
#         print("Hasil: ", hasil)

#     elif pilihan == "4":
#         i = float(input("Masukkan angka pertama: "))
#         j = float(input("Masukkan angka kedua: "))
#         hasil = bagi(i, j)
#         print("Hasil: ", hasil)

#     elif pilihan == "5":
#         i = float(input("Masukkan angka pertama: "))
#         j = float(input("Masukkan angka kedua: "))
#         hasil = pangkat(i, j)
#         print("Hasil: ", hasil)

#     else:
#         print("Pilihan tidak valid. Silakan coba lagi.")
#         continue

#     while True:
#         lanjut = input("Apakah Anda ingin melanjutkan? (y/n): ")
#         if lanjut.lower() == "y" or lanjut.lower() == "n":
#             break
#         else:
#             print("Input tidak valid. Silakan masukkan 'y' untuk melanjutkan atau 'n' untuk selesai.")

#     if lanjut.lower() == "n":
#         print("Terima kasih!")
#         break


#dengan method procedure
def tambah(i, j):
    hasil = i + j
    print("Hasil: ", hasil)

def kurang(i, j):
    hasil = i - j
    print("Hasil: ", hasil)

def kali(i, j):
    hasil = i * j
    print("Hasil: ", hasil)

def bagi(i, j):
    hasil = i / j
    print("Hasil: ", hasil)

def pangkat(i, j):
    hasil = i ** j
    print("Hasil: ", hasil)

def kalkulator():
    while True:
        print("             KALKULATOR")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Pangkat")

        pilihan = input("Masukkan pilihan : ")

        if pilihan == "1":
            i = float(input("Masukkan angka pertama: "))
            j = float(input("Masukkan angka kedua: "))
            tambah(i, j)

        elif pilihan == "2":
            i = float(input("Masukkan angka pertama: "))
            j = float(input("Masukkan angka kedua: "))
            kurang(i, j)

        elif pilihan == "3":
            i = float(input("Masukkan angka pertama: "))
            j = float(input("Masukkan angka kedua: "))
            kali(i, j)

        elif pilihan == "4":
            i = float(input("Masukkan angka pertama: "))
            j = float(input("Masukkan angka kedua: "))
            bagi(i, j)

        elif pilihan == "5":
            i = float(input("Masukkan angka pertama: "))
            j = float(input("Masukkan angka kedua: "))
            pangkat(i, j)

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            continue

        while True:
            lanjut = input("Apakah Anda ingin melanjutkan? (y/n): ")
            if lanjut.lower() == "y" or lanjut.lower() == "n":
                break
            else:
                print("Input tidak valid. Silakan masukkan 'y' untuk melanjutkan atau 'n' untuk selesai.")

        if lanjut.lower() == "n":
            print("Terima kasih!")
            break

kalkulator()
