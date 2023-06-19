def binary_search(keyword, data):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == keyword:
            return mid
        elif data[mid] < keyword:
            left = mid + 1
        else:
            right = mid - 1
    return -1

data = [17, 2, 15, 7, 72, 31, 12, 57, 63, 71, 23, 92, 1]
keyword = 72

data.sort()

result = binary_search(keyword, data)

if result != -1:
    print("Angka 72 ditemukan di indeks", result)
else:
    print("Angka 72 tidak ditemukan dalam daftar bilangan acak.")

