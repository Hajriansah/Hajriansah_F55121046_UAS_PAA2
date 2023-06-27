# Hajriansah
# F55121046
# Kelas B

import time

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()
    iterations = []
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        iterations.append(arr.copy())
        if not swapped:
            break
    end_time = time.time()
    return arr, iterations, end_time - start_time

def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()
    iterations = []
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        iterations.append(arr.copy())
    end_time = time.time()
    return arr, iterations, end_time - start_time

def print_iterations(iterations, sort_type, iterations_count=5):
    print(f"\n{sort_type} - {iterations_count} Iterasi Pertama:")
    for i in range(min(iterations_count, len(iterations))):
        print(iterations[i])
    print("\n")

    print(f"{sort_type} - {iterations_count} Iterasi Terakhir:")
    for i in range(max(0, len(iterations) - iterations_count), len(iterations)):
        print(iterations[i])
    print("\n")

def print_computation_time(time):
    print(f"Waktu Komputasi: {time:.6f} detik")

def main():
    arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7, 26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21,
           23, 63, 84, 32, 5, 3, 44, 21, 10, 21, 17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59, 40, 7, 41, 81]

    while True:
        print("Sebelum pengurutan:")
        print(arr)
        sort_type = input("\nPilih metode pengurutan (bubble sort / insertion sort) atau ketik 'exit' untuk keluar: ")

        if sort_type.lower() == "exit":
            break
        elif sort_type.lower() == "bubble sort":
            sorted_arr, iterations, time_taken = bubble_sort(arr.copy())
        elif sort_type.lower() == "insertion sort":
            sorted_arr, iterations, time_taken = insertion_sort(arr.copy())
        else:
            print("Maaf, tipe pengurutan yang Anda masukkan tidak valid.")
            continue

        print("\nSetelah pengurutan:")
        print(sorted_arr)
        print_iterations(iterations, sort_type)
        print_computation_time(time_taken)

if __name__ == "__main__":
    main()
