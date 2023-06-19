#dengan method function
def masukkan_bilangan(angka):
    if angka % 2 == 0:
        return "genap"
    else:
        return "ganjil"

bilangan = int(input("Masukkan bilangan: "))
hasil = masukkan_bilangan(bilangan)

print(f"Bilangan yang anda masukkan adalah bilangan {hasil}.")

#dengan method procedure
def masukkan_bilangan(angka):
    if angka % 2 == 0:
        print("Bilangan yang anda masukkan adalah bilangan genap.")
    else:
        print("Bilangan yang anda masukkan adalah bilangan ganjil.")

bilangan = int(input("Masukkan bilangan: "))
masukkan_bilangan(bilangan)
