print("=====mencari kpk=====")

def fpb(a, b):
    while b:
        a, b = b, a % b
    return a


def kpk(a, b):
    return a*b // fpb(a, b)

bil1 = int(input("Masukkan bilangan pertama: "))
bil2 = int(input("Masukkan bilangan kedua: "))
print("kpk= ",kpk(bil1, bil2))




