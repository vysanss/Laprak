def binary_search(keyword, data):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        if data[mid] == keyword:
            return True
        elif data[mid] < keyword:
            left = mid + 1
        else:
            right = mid - 1

    return False

nim_list = [20103023, 20103002, 20103019, 20103001, 20103017, 20103005, 20103011, 20103003, 20103009, 20103021, 20103006, 20103015, 20103013, 20103007]
keyword = 20103015

nim_list.sort()

if binary_search(keyword, nim_list):
    print("NIM", keyword, "ditemukan di kelas.")
else:
    print("NIM", keyword, "tidak ditemukan di kelas.")
