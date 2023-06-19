
Nama_Lengkap = input("nama:")
TTL = input("ttl:")
Alamat = input("alamat:")
No_HP = input("no. hp:")
Prodi = input("prodi:")
Hobi = input("hobi:")

print("==========================")

print("Biodata Diri")
print("Nama : {}".format(Nama_Lengkap))
print("TTL : {}".format(TTL))
print("Alamat : {}".format(Alamat))
print("No.HP : {}".format(No_HP))
print("Prodi : {}".format(Prodi))
print("Hobi : {}".format(Hobi))
print("")
biodata = "Halo nama saya {}, kelahiran {}\n, alamat {}, No.HP : {}, Prodi {}, Hobi {}."
print(biodata.format(Nama_Lengkap,TTL,Alamat,No_HP,Prodi,Hobi))