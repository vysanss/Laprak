#perulangan while
i = 0
while i <= 7:
    print("hello world!")
    i += 1

#perulangan increment
a = 1
b = 10
while a < b:
    print("step ke-", a)
    a += 1

#perulangan decrement
a = 10
b = 0
while a > b:
    print("Kuota Internet tersisa", a, "GB")
    a -= 1

#break
for i in range(1, 10):
    print(f"ini perulangan ke- {i}")
    if i == 5:
        print(f"perulangan ke-", i, "terhenti")
        break

#continue
for i in range(0, 10):
    #skip jika i == 5
    if(i == 5):
        continue
    print(i)

#break pada perulangan while
a = 0
while True:
    print("step ke-", a, "!")
    a += 1
    if a == 7:
        print("step ke-", a, "dihentikan!")
        break

#continue pada perulangan while
angka = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

#skip jika i adalah bilangan genap
#dan i lebih dari 0
i = -1
while i < len(angka):
    i += 1
    if i % 2 == 0 and i > 0:
        print('skip')
        continue

#tidak dieksekusi ketika continue dipanggil
    print(angka[i])