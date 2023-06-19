def linear_search(keyword, data):
    for i in range(len(data)):
        if data[i] == keyword:
            return i
    return -1

database = ["R 2477 SR", "R 1234 DJ", "R 7015 LP", "R 0201 RR", "R 3304 DA", "R 2401 SK", "R 2103 RT", "R 1708 RI", "R 1111 SR", "R 4987 LH"]
keyword = "R 2488 SR"

result = linear_search(keyword, database)

if result != -1:
    print("Nomor plat ditemukan di indeks", result)
else:
    print("Nomor plat tidak ditemukan dalam database.")
