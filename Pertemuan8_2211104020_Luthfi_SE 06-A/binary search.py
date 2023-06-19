def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1 ):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

def binary_search(keyword, data):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] > keyword:
            right = mid - 1
        elif (data[mid]) < keyword:
            left = mid + 1
        else:
            print(data)
            print(f"Keyword {keyword} has been found at index {mid}")
            return mid
    print(f"Keyword {keyword} not found")
    return -1

data = [23, 3, 4, 78, 9, 10, 32]
bubble_sort(data)

keyword = int(input("Input keyword: "))
binary_search(keyword,data)
