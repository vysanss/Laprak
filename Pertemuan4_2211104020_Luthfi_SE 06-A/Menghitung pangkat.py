bil = int (input("Masukan bilangan= "))
pangkat = int (input("Masukan pangkat= "))
hasil = bil

for i in range (pangkat -1):
    hasil *= bil
    
print("Hasil pangkat= ", hasil)